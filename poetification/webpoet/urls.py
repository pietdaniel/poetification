from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns =\
    patterns('',
             url(r'^$', views.index, name='index'),
             url(r'^home/$', views.home, name='home'))
             # url(r'^new/$', views.new, name='new'))