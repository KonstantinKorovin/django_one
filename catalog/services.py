from catalog.models import Product


class CatalogService:

    """ Бизнес логика приложения 'Catalog' """

    @staticmethod
    def list_products(category_id):
        return Product.objects.filter(category_id=category_id)
