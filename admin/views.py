from django.shortcuts import render
from django.views.generic import *

# Create your views here.

def login_user(request):
    pass

def logout_user(request):
    pass

def order_summary(request):
    '''
    :param request:
    :return:
    '''
    pass

class CustomerListView(ListView):
    pass

class CustomerDetail(DetailView):
    pass

class CustomerUpdate(UpdateView):
    pass

