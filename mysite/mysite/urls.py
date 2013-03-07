from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from books import views
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^hello/$', hello),
                       (r'^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^display_meta/$', display_meta),
                       (r'^search/$', views.search),
                       (r'^contact/$', views.contact),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
