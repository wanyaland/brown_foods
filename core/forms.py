__author__ = 'wanyama'

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput,EmailInput
from django import forms
from models import BillingDetails,Customer

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1':TextInput(attrs={'class':'form-control','placeholder': 'Password'}),
            'password2':TextInput(attrs={'class': 'form-control','placeholder': 'Repeat Password'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = BillingDetails

class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('email','is_active','first_name','last_name')
        widgets = {
            'email': TextInput(),
        }

