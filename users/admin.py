from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "country", "is_staff", "is_superuser")
    list_filter = ("country", "username")
    search_fields = ("email", "phone_number", "country")


