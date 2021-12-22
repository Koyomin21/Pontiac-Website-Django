from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('history/', views.history, name="history"),
    path('booking/', views.car_catalog, name="car_catalog"),
    path('accessories/',views.accessories_catalog, name='accessories_catalog'),
    path('accessories/cartOrder/',views.part_order,name='part_order'),
    path('booking/cartOrder/',views.car_order,name='car_order'),
    path('success/car',views.orderCar,name="successCar"),
    path('success/part',views.orderPart,name="successPart")
]
