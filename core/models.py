from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BillingDetails(models.Model):
    first_name  = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    company = models.CharField(max_length=100,null=True)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_number = models.CharField(max_length=20)
    order_notes = models.TextField()

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
    payment_id = models.CharField(max_length=20,null=True )

    def add_to_cart(self,item_id):
        item = MenuItem.objects.get(pk=item_id)
        try:
            preexisting_order = CartItem.objects.get(menu_item=item,cart=self)
            preexisting_order.quantity +=1
            preexisting_order.save()
        except CartItem.DoesNotExit:
            new_order = CartItem.objects.create(
                menu_item=item,
                cart = self,
                quantity=1
            )
            new_order.save()
    def remove_from_cart(self,item_id):
        item = MenuItem.objects.get(pk=item_id)
        try:
            preexisting_order = CartItem.objects.get(menu_item=item,cart=self)
            if preexisting_order.quantity>1:
                preexisting_order.quantity -=1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except CartItem.DoesNotExist:
            pass

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brown_food/%Y/%m/%d',null=True)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    cart = models.ForeignKey(Cart)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    def total_price(self):
        return self.unit_price*self.quantity













