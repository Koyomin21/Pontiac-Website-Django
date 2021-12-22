from django.http.response import HttpResponse
from django.shortcuts import render
from .models import AutoPart, CarImage, PartImage
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
    
    cars = [ {'id':i.car_id,'name':i.name, 'price': i.price, 'image': car_images.filter(car__car_id=i.car_id).first() } for i in fetched_cars ]
    rows = range(len(cars)//3 + len(cars)%3*1)
    print(rows)

    context = {
        'cars': cars,
        'rows': rows
    }

    return render(request, 'cars.html', context)

def accessories_catalog(request):

    fetched_parts = AutoPart.objects.all()
    part_images = PartImage.objects.all()

    parts = [{
        'id':i.part_id,
        'name': i.name,
        'price': i.price,
        'image':  part_images.filter(part__part_id=i.part_id).first()
    } for i in fetched_parts ]

    rows = range(len(parts)//3 + len(parts)%3*1)
    print(rows)

    context = {
        'parts': parts,
        'rows': rows
    }
    print(part_images)
    print(parts[0]['image'].path)
    return render(request, 'accessories.html', context)


def part_order(request):
    partId= request.GET.get('id')
    part = AutoPart.objects.get(pk=partId)

    part_images = PartImage.objects.all()
    partImg = part_images.filter(part__part_id=partId).first()
    context ={
        'name':part.name,
        'image': partImg,
        'price':part.price,
        'description':part.description
    }
    return render(request, 'cart.html',context)

def car_order(request):
    carId = request.GET.get('id')
    car = Car.objects.get(pk=carId)

    car_images = CarImage.objects.all()

    context ={
        'name':car.name,
        'image': car_images.filter(car__car_id=carId).first(),
        'price':car.price,
        'description':'pontiac musclecar'
    }
    return render(request, 'cart.html',context)

