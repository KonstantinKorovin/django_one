from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    return HttpResponse("Данные отправлены на сервер!")

def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html")
    return HttpResponse("Данные отправлены на сервер!")