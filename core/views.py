from django.shortcuts import render,redirect
from .models import CartItem,MenuItem,BillingDetails
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist
from cart import Cart

# Create your views here.

def home(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items':menu_items,
    }
    return render(request,'core/home.html',context)

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')

    return render(request,'core/checkout.html')


def cart(request):
    return render(request,'core/cart.html',{
        'cart':Cart(request)
    })


def checkout(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        order_notes = request.POST.get('order')
        billing_details = BillingDetails()
        billing_details.first_name = first_name
        billing_details.last_name =last_name
        billing_details.company = company
        billing_details.phone_number = phone
        billing_details.email = email
        billing_details.address_line1 = add1
        billing_details.address_line2 = add2
        billing_details.order_notes = order_notes
        billing_details.save()
        cart = Cart(request)
        cart.billing_details = billing_details
        return render(request,'core/payment.html',{
            'cart':Cart(request),
        })
    else:
         return render(request,'core/checkout.html',{
        'cart':Cart(request),
    })



def add_to_cart(request,menu_id,quantity):
    menu_item= MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.add(menu_item,menu_item.unit_price,quantity)
    return render(request,'core/cart.html',{
        'cart':cart,
    })

def update_cart(request,menu_id,quantity):
    menu_item = MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.update(menu_item,quantity)
    return render(request,'core/cart.html',{
        'cart':cart,
    })

def remove_from_cart(request,menu_id):
    menu_item = MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.remove(menu_item)
    return render(request,'core/cart.html',{
        'cart':cart,
    })

def process_payment(request):
    pass

class MenuList(ListView):
    model = MenuItem
    template_name = 'core/menu_list.html'




