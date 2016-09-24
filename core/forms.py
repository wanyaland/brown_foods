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
        model = Customer

class CustomerChangeForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('email','first_name','last_name','address_line1','address_line2',)
        widgets = {
            'email': TextInput(),
        }


class CustomerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email','address_line1','address_line2')

    def clean_password2(self):
        password1 = self.clanead_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords dont match")
        return password2

    def save(self,commit=True):
        customer = super(CustomerCreationForm,self).save(commit=False)
        customer.set_password(self.cleaned_data["password1"])
        if commit:
            customer.save()
        return customer

class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=("Email"),max_length=200)

