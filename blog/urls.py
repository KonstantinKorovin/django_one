from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, HomeView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("home_blog/", HomeView.as_view(), name="home_blog"),
    path("blogs/blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
