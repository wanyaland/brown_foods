from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.customer_name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='brown_food/%Y/%m/%d')
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    customer = models.OneToOneField(Customer)

class OrderLine(models.Model):
    menu_item = models.OneToOneField(MenuItem)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order)

    def line_total(self):
        return self.menu_item.price * self.quantity







