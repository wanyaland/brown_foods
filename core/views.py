from django.shortcuts import render,redirect
from .models import Cart,Order,MenuItem,Customer
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def home(request):
    return render(request,'core/home.html')

def cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objecs.filter(customer=customer)
        orders = Order.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.menu_item.price*order.quantity)
            count += order.quantity
        context = {
            'orders':orders,
            'total':total
        }
        return render(request,'core/cart.html',context)
    else :
        redirect('core:home')

def checkout(request):
    return render(request,'core/checkout.html')

def add_to_cart(request,menu_id):
  if request.user.is_authenticated:
    try:
        item = MenuItem.objects.get(pk=menu_id)
    except ObjectDoesNotExist:
        pass
    else:
        customer = Customer.get(user=request.user)
        try:
            cart = Cart.objects.get(active=True,customer=customer)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(customer=customer)
            cart.save()
        cart.add_to_cart(menu_id)
    return redirect('core:cart')
  else:
      return redirect('core:home')

def remove_from_cart(request,menu_id):
    pass

class MenuList(ListView):
    model = MenuItem
    template_name = 'core/menu_list.html'




