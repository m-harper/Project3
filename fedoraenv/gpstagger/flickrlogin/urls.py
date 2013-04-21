from django.conf.urls.defaults import *
from models import photo_grabber

info_dict = {
	'queryset': photo_grabber.objects.all()
}

urlpatterns = patterns('',
   # (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
)