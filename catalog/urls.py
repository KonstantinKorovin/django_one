from django.urls import path
from catalog.views import (
    home,
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("products/create", ProductCreateView.as_view(), name="products_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
