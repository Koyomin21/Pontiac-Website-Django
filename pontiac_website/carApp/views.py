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
    
    cars = [
        {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
        {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
        {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
        {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
         {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
         {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
        {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        },
         {
            'name':'PONTIAC GTO',
            'price':5050,
            'image_path':'images/car.jpg'
        }
    ]
    rows = range(len(cars)//3 + len(cars)%3*1)
    print(rows)

    context = {
        'cars': cars,
        'rows': rows
    }

    return render(request, 'cars.html', context)
