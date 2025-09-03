from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product
from catalog.forms import ProductForm


# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, "home_blog.html")
    return HttpResponse("Данные отправлены на сервер!")


def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html")
    return HttpResponse("Данные отправлены на сервер!")


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.can_unpublish_product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["owner"] = self.request.user == product.owner
        return context

    def form_valid(self, form):
        product = self.get_object()
        if self.request.user != product.owner or not self.request.user.has_perm("can_unpublish_product"):
            return HttpResponseForbidden("У вас недостаточно прав для редактирования продукта.")
        return super().form_valid(form)


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.can_remove_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["owner"] = self.request.user == product.owner
        return context

    def form_valid(self, form):
        product = self.get_object()
        if self.request.user != product.owner or not self.request.user.has_perm("can_remove_product"):
            return HttpResponseForbidden("У вас недостаточно прав для удаления продукта.")
        return super().form_valid(form)
