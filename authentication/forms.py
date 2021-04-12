from django import forms
from django.forms import PasswordInput

from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = {'first_name', 'middle_name', 'last_name', 'email', 'password'}
        widgets = {
            'password': PasswordInput()
        }
