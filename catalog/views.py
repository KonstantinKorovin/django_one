from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    return HttpResponse("Данные отправлены на сервер!")


def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html")
    return HttpResponse("Данные отправлены на сервер!")


def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products_list.html", context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context=context)
