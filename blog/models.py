from django.db import models


# Create your models here.
class BlogModel(models.Model):
    """
    Модель Блога
    """

    header = models.CharField(
        max_length=100,
        null=False,
        help_text="Введите заголовок",
        verbose_name="Заголовок",
    )
    description = models.TextField(verbose_name="Текст статьи", null=False)
    preview = models.ImageField(
        upload_to="blog/photo/",
        help_text="Загрузите изображение",
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата создания"
    )
    is_publication = models.BooleanField(verbose_name="Cтатус публикации")
    views_count = models.IntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Мой личный блог"

        ordering = ["created_at", "views_count"]

    def __str__(self):
        return self.header
