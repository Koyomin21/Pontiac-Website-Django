from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    price = models.BigIntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=70)
    startDate = models.DateField(auto_now=True)
    endDate = models.DateField()
    

class CarImage(models.Model):
    img_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    path = models.TextField()

class PartCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class AutoPart(models.Model):
    part_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="Something")
    description = models.TextField()
    quantity = models.IntegerField()

class PartImage(models.Model):
    img_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(AutoPart, on_delete=models.CASCADE)
    path = models.TextField()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    price = models.BigIntegerField()
    order_date = models.DateField(auto_now=True)
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=150)

class PartOrder(models.Model):
    part = models.ForeignKey(AutoPart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
