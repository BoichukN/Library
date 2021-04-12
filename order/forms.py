from django import forms
from django.forms import DateTimeInput

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'user', 'book', 'plated_end_at'}
        widgets = {
            "plated_end_at": DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }
