from django.conf.urls import patterns, url

from flickr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)