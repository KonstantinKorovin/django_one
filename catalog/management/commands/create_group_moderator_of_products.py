from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):

    help = "Создание группы 'ProductModerators' "

    def handle(self, *args, **options):
        product_moderators, created = Group.objects.get_or_create(
            name="ProductModerators"
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Группа {product_moderators.name} успешно создана!")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Группа {product_moderators.name} уже существует!")
            )

        can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
        can_remove_product = Permission.objects.get(codename="can_remove_product")

        product_moderators.permissions.add(can_unpublish_product, can_remove_product)

        self.stdout.write(
            self.style.SUCCESS(
                f"Права '{can_unpublish_product.name}' и '{can_remove_product.name}' успешно добавлены!"
            )
        )
