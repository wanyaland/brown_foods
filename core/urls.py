__author__ = 'wanyama'

from django.conf.urls import patterns,url
from core.views import *
from django.contrib.staticfiles.urls import static

urlpatterns = patterns('',
                       url(r'^$',home,name='home'),
                       url(r'^register/$',register,name='register'),
                       url(r'^cart/$',cart,name='cart'),
                       url(r'^add_to_cart/$',add_to_cart,name='add_to_cart'),
                       #url(r'^update_cart/(?P<menu_id>\d+)/(?P<quantity>\d+)/$',update_cart,name='update_cart'),
                       url(r'^remove_from_cart/$',remove_from_cart,name='remove_from_cart'),
                       url(r'^order/$',order,name='order'),
                       url(r'^process_checkout/$',process_checkout,name='process_checkout'),
                       url(r'^checkout/$',checkout,name='checkout'),
                       url(r'^payment',payment,name='payment'),
                       url(r'^about_us/$',about_us,name='about_us'),
                       url(r'^menus/(?P<pk>[0-9]+)/$',MenuDetail.as_view(),name='menu-detail'),
                       url(r'^how-it-works/$',how_it_works,name='how-it-works'),
                       url(r'^menu/$',menu,name='menu'),
                       url(r'^login/$',login_customer,name='login'),
                       url(r'^logout/$',logout_customer,name='logout-customer'),
                       url(r'^process-order/$',process_order,name='process-order'),
                       url(r'^order-summary/$',order_summary,name='order-summary'),
                       url(r'^view-account/(?P<pk>\d+)/$',ViewAccount.as_view(),name='my-account'),
                       url(r'^edit-account/(?P<pk>\d+)/$',EditAccount.as_view(),name='edit-account'),
                       url(r'^delivery_charged/$',delivery_charged,name='delivery_charged'),
                       url(r'^deposit/$',deposit,name='deposit'),
                       url(r'^process-deposit/$',process_deposit,name='process-deposit'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
