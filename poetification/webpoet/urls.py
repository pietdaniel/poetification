from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns =\
    patterns('',
			url(r'^$', views.index, name='index'),
			url(r'^home/$', views.home, name='home'),
			url(r'^access/$', views.access, name='access'),
			url(r'^complete/twitter/$', views.auth, name='auth'),
			url(r'', include('social_auth.urls')))
    		# url(r'login/facebook/', include('social_auth.urls')))
             # url(r'^new/$', views.new, name='new'))