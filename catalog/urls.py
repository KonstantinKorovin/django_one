from django.urls import path
from catalog.views import home, contacts, products_list, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", products_list, name="products_shop"),
    path("products/<int:pk>", product_detail, name="product_detail"),
]
