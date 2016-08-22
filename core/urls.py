__author__ = 'wanyama'

from django.conf.urls import patterns,url
from core.views import *

urlpatterns = patterns('',
    url(r'^',home,name='home'),
)
