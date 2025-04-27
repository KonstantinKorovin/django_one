from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add Products and Categories in database"

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(name="Фрукты")
        category2, _ = Category.objects.get_or_create(name="Овощи")

        db_products = [
            {"name": "Яблоко", "description": "Описание1", "image": "яблоко.png", "category": category1, "price": 150},
            {"name": "Ананас", "description": "Описание2", "image": "ананас.png", "category": category1, "price": 160},
            {"name": "Помидор", "description": "Описание3", "image": "помидор.png", "category": category2, "price": 130},
            {"name": "Огурец", "description": "Описание4", "image": "огурец.png", "category": category2, "price": 140},
        ]

        for product in db_products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Успешное создание продукта: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт: {product.name} не был создан!"))