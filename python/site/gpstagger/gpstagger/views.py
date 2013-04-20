#needed for all views
from django.http import HttpResponse
#template functions, replaced with shortcut
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
#google map django bindings
from django.contrib.gis.maps.google.gmap import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GEvent
#database types
from gpstagger.models import picture, make_picture
#simple json de/serializers
from django.core import serializers

#used for DB actions
import sqlite3

import json

#tutorial for simple views
#http://www.djangobook.com/en/2.0/chapter03.html

#views receives some HttpResponse and returns an HttpResponse
def hello(request):
	return HttpResponse("Hello world")

#Django gmap tutorial:
#http://jefurii.cafejosti.net/blog/2011/05/05/basic-google-maps-django/
#GEOS required for gis
#https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/geolibs/
#GeoDjango library reference
#https://docs.djangoproject.com/en/dev/ref/contrib/gis/
#GoogleMap source
#https://github.com/django/django/blob/master/django/contrib/gis/maps/google/gmap.py
def gmapfunc(request):
	#conn = sqlite3.connect('picture.db')
	#c = conn.cursor()

	#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	#print(c.fetchall())

	#data = make_picture( 'default_', '35.42', '139.42', 'http://127.0.0.1:8000/hello/')
	#c.execute("DROP TABLE picturesTable ")
	#c.execute("CREATE TABLE picturesTable (name, json)")
	#c.execute('INSERT INTO picturesTable VALUES (?,?)', [ data['name'], json.dumps( data, sort_keys=True, indent=1), ] )

	#conn.commit()

	##access DB and get all JSON objects that are pictures
	#c.execute("SELECT json FROM picturesTable")
	#pictures = c.fetchall()

	#print "PICTURES"
	#print pictures
	#print "END PICTURES"
	##make python array of those objects converted to python
	##pics = serializers.serialize( "json", make_picture( 'default_', '35.42', '139.42', 'http://127.0.0.1:8000/hello/'))
	#py_pictures = []
	#for x in range(0,len(pictures)):
		#py_pictures.append(json.loads(pictures[x][0]))

	##plot
	#markers = []
	#for pic in py_pictures:
		#marker = GMarker('POINT(%s %s)' % (pic['lon'], pic['lat']))
		#event = GEvent('click', 'function() { location.href = "%s"}' % pic['href'])
		#marker.add_event(event)
		#markers.append(marker)
	#gmap = GoogleMap(center=(0,0), zoom=1, markers=markers, key='AIzaSyBI2r_ZwESKtz3jMuwEpVAkzu1M0qeOJAw')

	#usr clicking on marker should show image

	points = [ {'lat':'35.42', 'lng':'139.42', 'href':'http://127.0.0.1:8000/hello/'}, ]
	markers = []
	for point in points:
		marker = GMarker('POINT(%s %s)' % (point['lng'], point['lat']))
		event = GEvent('click', 'function() { location.href = "%s"}' % point['href'])
		marker.add_event(event)
		markers.append(marker)
	gmap = GoogleMap(center=(0,0), zoom=1, markers=markers, key='AIzaSyBI2r_ZwESKtz3jMuwEpVAkzu1M0qeOJAw')

	return render_to_response('map.html', {'gmap':gmap,})

#	{{ gmap.style }}
#	{{ gmap.scripts }}
