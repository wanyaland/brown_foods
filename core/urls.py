__author__ = 'wanyama'

from django.conf.urls import patterns,url
from core.views import *

urlpatterns = patterns('',
                       url(r'^$',home,name='home'),
                       url(r'^cart/(?P<cart_id>[0-9]+)/',cart,name='cart'),
                       url(r'^menu_items/$',MenuList.as_view(),name='menu_items'),
                       url(r'^checkout/$',checkout,name='checkout')
)
