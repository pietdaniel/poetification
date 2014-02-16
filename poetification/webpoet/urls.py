from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns =\
    patterns('',
             url(r'^$', views.index, name='index'),
             url(r'^home/$', views.home, name='home'),
             url(r'^twaccess/$', views.twaccess, name='twaccess'),
             url(r'^fbaccess/$', views.fbaccess, name='fbaccess'),
             url(r'^ghaccess/$', views.ghaccess, name='ghaccess'),
             url(r'^complete/twitter/$', views.twauth, name='twauth'),
             url(r'^complete/facebook/$', views.fbauth, name='fbauth'),
             url(r'^complete/github/$', views.ghauth, name='ghauth'),
             url(r'', include('social_auth.urls')))
