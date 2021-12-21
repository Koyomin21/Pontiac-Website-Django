from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('history/', views.history, name="history"),
    path('booking/', views.car_catalog, name="car_catalog")

]
