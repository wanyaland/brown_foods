from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brown_food.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       url(r'^',include('core.urls',namespace='core')),
                       url(r'^admin/',include('admin.urls',namespace='admin')),
)
