from django import forms
from django.forms import fields
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['price', 'delivery_address', 'delivery_date']

