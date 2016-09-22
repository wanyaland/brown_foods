from django.shortcuts import render,redirect
from .models import CartItem,MenuItem,BillingDetails, Customer,PesaPal
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
import requests


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

def checkout(request):
    if request.method=='POST':
        cart = Cart(request)
        delivery_fee = request.GET.get('delivery_fee')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address1 = request.POST.get('add1')
        address2= request.POST.get('add2')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        billing_details = BillingDetails(first_name=first_name,last_name=last_name,email=email,phone_number=phone1,
                                         phone_number2=phone2,address_line1=address1,address_line2=address2)
        billing_details.save()
        cart.billing_details = billing_details
        cart.save()
        client = pesapal.PesaPal("Au93fiwr5A/NhPZqesxbjVNDqzFBdMI+","d00fVQICYG8f/3kxueNRKQkfXnk=",False)
        if delivery_fee:
            total_cost = cart.summary()+ 5000
        else :
            total_cost = cart.summary()

        request_data = {
            'FirstName':first_name,
            'LastName':last_name,
            'Email':email,
            'Amount':str(total_cost),
            'Description':'Buying food from Brown foods',
            'Type':'MERCHANT',
            'Reference': str(datetime.datetime.now()),
            'Currency':'UGX',
        }
        post_params = {
            'oauth_callback': 'http://brown.co.ug/process-order'
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
    items = []
    for cart_item in cart:
        item = {}
        item['id']= cart_item.id
        item['name'] = cart_item.menu_item.name
        item['quantity']= cart_item.quantity
        item['price']= cart_item.unit_price
        items.append(item)
    total = cart.summary()
    data={"items":items,"total":str(total),}
    return HttpResponse(json.dumps(data))

def remove_from_cart(request):
    menu_id = request.POST.get('menu_id')
    menu_item = MenuItem.objects.get(id=menu_id)
    cart = Cart(request)
    cart.remove(menu_item)
    data = {'success':'true'}
    return HttpResponse(json.dumps(data),content_type="application/json")

def my_account(request):
    return render(request,'core/my_account.html')

def order_summary(request):
    return render(request,'core/order_summary.html')

def process_order(request):
    '''
    Handle the callback from PesaPal
    '''
    cart = Cart(request)
    tracking_id = request.GET.get('pesapal_transaction_tracking_id', '')
    reference = request.GET.get('pesapal_merchant_reference', '')
    if tracking_id and reference:
        params = {
            'pesapal_merchant_reference': reference,
            'pesapal_transaction_tracking_id': tracking_id
        }
        client = pesapal.PesaPal("Au93fiwr5A/NhPZqesxbjVNDqzFBdMI+","d00fVQICYG8f/3kxueNRKQkfXnk=",False)
        pesapal_request = client.queryPaymentStatus(params)
        url = pesapal_request.to_url()
        print url
        pesapal_response = requests.get(url)
        pesapal_response_data = pesapal_response.text
        pesapal_status = pesapal_response_data.split("=")[1]

        if pesapal_status == 'COMPLETED':
            state="Transaction was successful"
            cart.checked_out = True
            cart.save()
        else:
            state = "Transaction is %s" % pesapal_status

        p_ref = PesaPal(tracking_id=tracking_id,reference=reference,status=pesapal_status,cart=cart)
        p_ref.save()

    return render(request,'core/process-order.html',{
        'state':state,
    })

class MenuList(ListView):
    model = MenuItem
    template_name = 'core/menu_list.html'

class MenuDetail(DetailView):
    model = MenuItem
    template_name = 'core/product-detail.html'

def how_it_works(request):
    return render(request,'core/how-it-works.html')

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



