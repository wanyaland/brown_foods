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
from django_pesapal.views import PaymentRequestMixin


# Create your views here.

class PaymentView(PaymentRequestMixin):
    def get_pesapal_payment_iframe(self):
        '''
        Authenticates with pesapal to get the payment iframe src
        '''
        order_info = {
            'first_name':'Some',
            'last_name':'Other',
            'amount':100,
            'description': 'Payment',
            'reference':2,
            'email': 'wanyaland@gmail.com',
        }
        iframe_src_url = self.get_payment_url(**order_info)
        return iframe_src_url

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
    '''
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
        api_call(cart)
        cart.billing_details = billing_details
        return render(request,'core/payment.html',{
            'cart':cart,
        })
    else:
         return render(request,'core/checkout.html',{
        'cart':Cart(request),
    })
    '''

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
    data={'success':'true','menu_name':menu_item.name,'quantity':quantity,'menu_price':str(menu_item.unit_price),'menu_image':menu_item.image.url}
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



