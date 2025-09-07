from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.cache import cache
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product, Category
from catalog.forms import ProductForm
from catalog.services import CatalogService


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
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("products")

        if not queryset:
            queryset = super().get_queryset()
            cache.set("products", queryset, 60*15)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_counter += 1
        self.object.save()
        cache.delete(f"product_{self.object.id}")
        cache.set(f"product_{self.object.id}", self.object, timeout=900)
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        cache.delete("products")
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
        cache.delete("products")
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
        cache.delete("products")
        return super().form_valid(form)


class ProductByCategoryListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/product_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        queryset = CatalogService.list_products(category_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.kwargs.get("pk")
        if category_id:
            context['category'] = get_object_or_404(Category, pk=category_id)
        return context
