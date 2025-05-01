from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)

from blog.models import BlogModel


# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, "home_blog.html")
    return "Данные отправлены на сервер"


class BlogListView(ListView):
    model = BlogModel
    template_name = "blogs/blog_list.html"

    def get_queryset(self):
        return BlogModel.objects.filter(is_publication=True)


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = "blogs/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = BlogModel
    fields = (
        "header",
        "description",
        "preview",
        "created_at",
        "is_publication",
        "views_count",
    )
    template_name = "blogs/blog_create.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = BlogModel
    fields = (
        "header",
        "description",
        "preview",
        "created_at",
        "is_publication",
        "views_count",
    )
    template_name = "blogs/blog_create.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
