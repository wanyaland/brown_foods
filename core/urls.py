__author__ = 'wanyama'

from django.conf.urls import patterns,url
from core.views import *

urlpatterns = patterns('',
                       url(r'^$',home,name='home'),
                       url(r'^signup/$',signup,name='signup'),
                       url(r'^cart/$',cart,name='cart'),
                       url(r'^add_to_cart/$',add_to_cart,name='add_to_cart'),
                       #url(r'^update_cart/(?P<menu_id>\d+)/(?P<quantity>\d+)/$',update_cart,name='update_cart'),
                       url(r'^remove_from_cart/(?P<menu_id>\d+)/$',remove_from_cart,name='remove_from_cart'),
                       url(r'^menu_items/$',MenuList.as_view(),name='menu_items'),
                       url(r'^checkout/$',checkout,name='checkout'),
                       #url(r'^basket/$',show_basket),
                       url(r'^about_us/$',about_us,name='about_us'),
                       url(r'^menus/(?P<pk>[0-9]+)/$',MenuDetail.as_view(),name='menu-detail'),
)
