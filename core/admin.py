from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin
from .models import MenuItem
from .models import Customer

# Register your models here.
admin.site.register(MenuItem)




