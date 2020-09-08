from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["bus"]
        
class UserDriver(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]