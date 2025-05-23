from django.db import models


class Category(models.Model):
    """
    Модель категории
    """

    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
    )
    description = models.TextField(verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    """
    Модель продукта
    """

    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
    )
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="products/photo/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Название категории",
        null=True,
        blank=True,
        related_name="names",
    )
    price = models.IntegerField(
        verbose_name="Цена продукта"
    )
    created_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата обновления"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"
