from django.shortcuts import render,redirect
from .models import CartItem,MenuItem,BillingDetails, Customer
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist
from cart import Cart
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
import urllib
import time
import datetime
from django.conf import settings
import pesapal


# Create your views here.

def login_customer(request):
    email = password = next_url = state = ''
    if request.GET:
        next_url = request.GET.get('next')
    if request.POST:
        next_url = request.POST.get('next')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect('core:home')
            else:
                state = "Your account is not active"
        else:
            state = "Your email and password do not match"
    return render(request, 'core/login.html', {'state': state, 'email': email, 'password': password, 'next': next_url, })

def logout_customer(request):
    logout(request)
    return redirect('core:home')

def register(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        customer = Customer()
        customer.email = email
        customer.password = password
        customer.save()
    return render(request,'core/login.html')

def home(request):
    return render(request,'core/home.html')

def about_us(request):
    return render(request,'core/about-us.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')

    return render(request,'core/checkout.html')


def cart(request):
    return render(request,'core/cart.html',{
        'cart':Cart(request)
    })

def update_cart(request):
    pass

def process_checkout(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        billing_details = BillingDetails()
        billing_details.first_name = first_name
        billing_details.last_name = last_name
        billing_details.email = email
        client = pesapal.PesaPal("Au93fiwr5A/NhPZqesxbjVNDqzFBdMI+","d00fVQICYG8f/3kxueNRKQkfXnk=",False)
        total_cost = 500
        request_data = {
            'FirstName':first_name,
            'LastName':last_name,
            'Email':email,
            'Amount':str(total_cost),
            'Description':'Buying food from Brown foods',
            'Email':'wanyaland@gmail.com',
            'Type':'MERCHANT',
            'Reference': str(datetime.datetime.now()),
            'Currency':'UGX',
        }
        post_params = {
            'oauth_callback': 'http://brown.co.ug/'
        }
        pesapal_request = client.postDirectOrder(post_params, request_data)
        return render(request,'core/payment.html',{
            'iframe_url':pesapal_request.to_url(),
        })

def payment(request):
    return render(request,'core/payment.html')

def checkout(request):
    return render(request,'core/checkout.html',{
        'cart':Cart(request),
    })

def add_to_cart(request):
    quantity = request.POST.get('quantity')
    menu_id = request.POST.get('menu_id')
    menu_item= MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.add(menu_item,menu_item.unit_price,quantity)
    total = cart.summary()
    data={'success':'true','menu_name':menu_item.name,'quantity':quantity,'menu_price':str(menu_item.unit_price),'total':str(total)}
    return HttpResponse(json.dumps(data))

def remove_from_cart(request):
    menu_id = request.POST.get('menu_id')
    menu_item = MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.remove(menu_item)
    data = {'success':'true'}
    return HttpResponse(json.dumps(data),content_type="application/json")

def process_payment(request):
    pass

class MenuList(ListView):
    model = MenuItem
    template_name = 'core/menu_list.html'

class MenuDetail(DetailView):
    model = MenuItem
    template_name = 'core/product-detail.html'

def how_it_works(request):
    return render(request,'core/how-it-works.html')

def complete(request):
    return render(request,'core/complete.html')

def menu(request):
    menu_items = MenuItem.objects.filter(menu_type='M')
    side_dishes = MenuItem.objects.filter(menu_type='S')
    context = {'menu_items':menu_items,'side_dishes':side_dishes,}
    return render(request,'core/menu.html',context)

def order(request):
    cart = Cart(request)
    menu_items = MenuItem.objects.filter(menu_type='M')
    side_dishes = MenuItem.objects.filter(menu_type='S')
    context = {'menu_items':menu_items,'side_dishes':side_dishes,'cart':cart,}
    return render(request,'core/menu_list.html',context)



