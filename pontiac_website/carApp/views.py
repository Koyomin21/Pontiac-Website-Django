from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def contacts(request):
    context = {}

    return render(request, 'contacts.html', context)


def history(request):
    context = {}

    return render(request, 'history.html', context)


def car_catalog(request):
    context = {}

    return render(request, 'cars.html', context)
