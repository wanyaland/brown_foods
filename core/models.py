from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.customer_name

class Cart(models.Model):
    PAYMENT_TYPE=(
        ('C','CASH'),
        ('V','VISA CARD'),
        ('M','MOBILE MONEY'),
    )
    user = models.ForeignKey(Customer)
    order_date = models.DateTimeField(null=True)
    active = models.BooleanField()
    payment_type = models.CharField(max_length=100,null=True,choices=PAYMENT_TYPE)
    payment_id = models.CharField(max_length=20,null=True )

    def add_to_cart(self,item_id):
        item = MenuItem.objects.get(pk=item_id)
        try:
            preexisting_order = Order.objects.get(menu_item=item,cart=self)
            preexisting_order.quantity +=1
            preexisting_order.save()
        except Order.DoesNotExit:
            new_order = Order.objects.create(
                menu_item=item,
                cart = self,
                quantity=1
            )
            new_order.save()
    def remove_from_cart(self,item_id):
        item = MenuItem.objects.get(pk=item_id)
        try:
            preexisting_order = Order.objects.get(menu_item=item,cart=self)
            if preexisting_order.quantity>1:
                preexisting_order.quantity -=1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except Order.DoesNotExist:
            pass

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='brown_food/%Y/%m/%d')
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()













