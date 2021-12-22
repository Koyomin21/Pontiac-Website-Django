from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Booking, Car, AutoPart, CarImage, PartImage
import math

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def contacts(request):
    context = {}

    return render(request, 'contacts.html', context)

def dealership(request):
    context = {}
    return render(request, "dealership.html", context)

def history(request):
    context = {}

    return render(request, 'history.html', context)

def insuranse(request):
    context = {}

    return render(request, "insurance.html", context)

def services(request):
    context = {}

    return render(request, "services.html", context)

def whyoriginal(request):
    context = {}

    return render(request, "whyoriginal.html", context)


def car_catalog(request):

    fetched_cars = Car.objects.all()
    car_images = CarImage.objects.all()
    
    
    cars = [ {'id':i.car_id,'name':i.name, 'price': i.price, 'image': car_images.filter(car__car_id=i.car_id).first() } for i in fetched_cars ]
    rows = range(math.ceil(len(cars)/3))
    print(rows)

    context = {
        'cars': cars,
        'rows': rows
    }

    return render(request, 'cars.html', context)



def loan(request):
    context = {}

    months = request.GET.get('months')
    cash = request.GET.get('cash')

    if cash is None or months is None:
        return render(request, "loans.html", {
            'outcome':"",
            'loan_amount': "",
            "month": 6
        })
 
    months = float(months)
    cash = float(cash)
    cash_return = cash+cash*0.1
    outcome = cash_return // months

    context = {
        'outcome':outcome,
        'loan_amount': int(cash),
        "month": int(months)
    }

    return render(request, "loans.html", context)


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

