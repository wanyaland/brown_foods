from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brown_food.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       url(r'^',include('core.urls',namespace='core')),
                       url(r'^payments/',include('django_pesapal.urls')),
                       url(r'^admin/',admin.site.urls),
)
