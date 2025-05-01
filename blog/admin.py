from django.contrib import admin

from blog.models import BlogModel


# Register your models here.


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "header", "created_at", "is_publication")
    list_filter = ("header", "is_publication")
    search_fields = ("header",)
