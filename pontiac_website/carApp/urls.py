from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('history/', views.history, name="history"),
    path('booking/', views.car_catalog, name="car_catalog"),
    path('dealership/', views.dealership, name="dealership"),
    path('loans/', views.loan, name="loans"),
    path('insurance/', views.insuranse, name="insurance"),
    path('services/', views.services, name="services"),
    path('whyoriginal/', views.whyoriginal, name="whyoriginal")
    

]
