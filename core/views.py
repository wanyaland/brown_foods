from django.shortcuts import render,redirect
from .models import CartItem,MenuItem,BillingDetails
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist
from cart import Cart
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
import urllib
import time
import datetime
import urllib2
try:
    from xml.etree import cElementTree as ElementTree
except ImportError,e:
    from xml.etree import ElementTree
from django.conf import settings


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

def api_call(cart):
    url = "https://www.pesapal.com/API/PostPesapalDirectOrderV4"
    root = ElementTree.Element('PesapalDirectOrderInfo')
    root.set('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")
    root.set('xmlns:xsd',"http://www.w3.org/2001/XMLSchema")
    root.set('amount',str(cart.summary))
    root.set('currency',str('UGX'))
    root.set('description','order payment for')
    root.set('type','MERCHANT')
    root.set('reference',str(1))
    root.set('firstname',str(cart.billing_details.first_name))
    root.set('lastname',str(cart.billing_details.last_name))
    root.set('email',str(cart.billing_details.email))
    root.set('xmlns',"http://www.pesapal.com")
    data = {
        'oauth_callback':'',
        'oauth_consumer_key':settings.PESAPAL_KEY,
        'oauth_nonce':str(datetime.datetime.now()),
        'oauth_signature':settings.PEASPAL_SECRET,
        'ouath_signature_method':'HMAC-SHA1',
        'oauth_timestamp':str(time.time()),
        'oauth_version':'1.0',
        'pesapal_request_data':ElementTree.dump(root)
    }
    request = urllib2.Request(url,urllib.urlencode(data),headers={'Content-Type': 'application/xml'})
    return urllib2.urlopen(request)

def process_checkout(request):
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


def payment(request):
    return render(request,'core/payment.html')

def checkout(request):
    return render(request,'core/checkout.html',{
        'cart':Cart(request),
    })

def add_to_cart(request):
    menu_id = request.POST['menu_id']
    menu_item= MenuItem.objects.get(id=menu_id)
    quantity = request.POST.get('quantity')
    cart = Cart(request)
    cart.add(menu_item,menu_item.unit_price,quantity)
    data={'success':'true'}
    return HttpResponse(json.dumps(data))

def remove_from_cart(request):
    menu_id = request.GET.get('id')
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

def menu(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items':menu_items}
    return render(request,'core/menu.html',context)



