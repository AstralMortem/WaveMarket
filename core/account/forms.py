
from django import forms
from django.conf import settings
from .models import Customer, Address
from django.contrib.auth.forms import UserCreationForm  

class SignUpForm(UserCreationForm):
    photo =forms.ImageField(widget = forms.FileInput(attrs = {"class": "button is-primary"}),required=False) 
    class Meta:
        model = Customer
        fields = ('photo','username', 'email', 'first_name', 'last_name')

class SetupForm(forms.ModelForm):
    photo =forms.ImageField(widget = forms.FileInput(attrs = {"class": "button is-primary"}),required=False) 
    class Meta:
        model = Customer
        fields = ('photo','username', 'email', 'first_name', 'last_name', 'birth_date')
        

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields ="__all__"
        
        
