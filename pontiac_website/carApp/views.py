from django.http.response import HttpResponse
from django.shortcuts import render
from .models import CarImage
from .models import Car


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
    
    # cars = [
    #     {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #     {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #     {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #     {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #      {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #      {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #     {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     },
    #      {
    #         'name':'PONTIAC GTO',
    #         'price':5050,
    #         'image_path':'images/car.jpg'
    #     }
    # ]

    fetched_cars = Car.objects.all()
    car_images = CarImage.objects.all()
    
    cars = [ {'name':i.name, 'price': i.price, 'image': car_images.filter(car__car_id=i.car_id).first() } for i in fetched_cars ]
    rows = range(len(cars)//3 + len(cars)%3*1)
    print(rows)

    context = {
        'cars': cars,
        'rows': rows
    }

    return render(request, 'cars.html', context)
