from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
   BaseUserManager,AbstractBaseUser
)
import datetime

# Create your models here.

class CoreUserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Users must have a valid email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_admin = True
        user.save(using=self._db)


class Customer(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    objects = CoreUserManager()
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class BillingDetails(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    company = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    address_line1 = models.TextField(null=True)
    address_line2 = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    phone_number = models.CharField(max_length=20,null=True)
    phone_number2 = models.CharField(max_length=20,null=True)
    order_notes = models.TextField(null=True)
    delivery_date = models.DateField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.user.username


class Cart(models.Model):
    PAYMENT_TYPE=(
        ('C','CASH'),
        ('V','VISA CARD'),
        ('M','MOBILE MONEY'),
    )
    billing_details = models.OneToOneField(BillingDetails,null=True)
    creation_date = models.DateTimeField(null=True)
    checked_out = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=100,null=True,choices=PAYMENT_TYPE)
    payment_id = models.CharField(max_length=20,null=True)


class MenuItem(models.Model):
    CATEGORY = (
        ('M','MAIN'),
        ('S','SIDE DISH'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brown_food/%Y/%m/%d',null=True,blank=True)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True)
    menu_type = models.CharField(null=True,choices=CATEGORY,max_length=100)
    content = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    cart = models.ForeignKey(Cart)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

    def total_price(self):
        return self.unit_price*self.quantity

class Basket(models.Model):
    product_id = models.IntegerField()












