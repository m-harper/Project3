from django.conf.urls import patterns, include, url
#import the hello world function
from gpstagger.views import hello, gmapfunc

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flickr/', include('flickr.urls')),

	#any url using hello/ runs the hello function
	#HOORAY REGEX!
	url(r'^hello/$', hello),
	url(r'^map/$', gmapfunc),
)
