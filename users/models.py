from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Модель 'Пользователь'"""

    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="users/photo/", blank=True, default="images/users/photo/default.png"
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=55, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email
