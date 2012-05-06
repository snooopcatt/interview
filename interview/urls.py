from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from interview import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'interview.views.home', name='home'),
    # url(r'^interview/', include('interview.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^main/', views.MainView.as_view(), name='main'),
     url(r'^ajax/(?P<model_name>\w+)/', views.JSONResponseView.as_view(), name='ajax'),
)
