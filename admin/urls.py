__author__ = 'Harold'

from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('',
                       url(r'^$',order_summary,name='order-summary'),
                       url(r'^customer-detail/(?P<pk>\d+)/$',CustomerDetail.as_view(),name='customer-detail'),
                       url(r'^customer-list/(?P<pk>\d+)/$',CustomerListView.as_view(),name='customer-list'),
                       url(r'^customer-update/(?P<pk>\d+)/$',CustomerUpdate.as_view(),name='customer-update'),
)