#needed for all views
from django.http import HttpResponse

#template function
from django.shortcuts import render_to_response

#google map django bindings
#from django.contrib.gis.maps.google.gmap import GoogleMap
#from django.contrib.gis.maps.google.overlays import GMarker, GEvent
from GoogleMap import GoogleMap, GMarker, GEvent

#database types
from gpstagger.models import picture, make_picture

#used for DB actions
import DataBaseFunctions as DBF

#views receives some HttpResponse and returns an HttpResponse
def hello(request):
	return HttpResponse("Hello world")

def gmapfunc(request):
	#clear for testing
	DBF.resetDB()
	#add two test points to DB as JSON
	DBF.addPicture( make_picture( 'default_', '10.42', '10.42', 'http://127.0.0.1:8000/hello/') )
	DBF.addPicture( make_picture( 'default_', '-10.42', '10.42', 'http://127.0.0.1:8000/hello/') )

	#get all the pictures fromt the DataBase (as Python Objects)
	pictures = DBF.getPictures()
	gmap = createGoogleMap( pictures )
	return render_to_response('map.html', {'gmap':gmap,})


#non-django GoogleMap v3 implementation. made to imitate django gis v2 version
def createGoogleMap( pictures ):
	markers = []
	for picture in pictures:
		marker = GMarker(picture['lon'], picture['lat'], picture['name'])
		event = GEvent('click', 'function() { location.href = "%s"}' % picture['href'])
		print event
		print event.action
		print event.trigger
		marker.add_event(event)
		markers.append(marker)
	return GoogleMap(center=(0,0), zoom=1, markers=markers, key='AIzaSyBI2r_ZwESKtz3jMuwEpVAkzu1M0qeOJAw')

#django GoogleMap v2 version
#def createGoogleMap( pictures ):
	#markers = []
	#for picture in pictures:
		#marker = GMarker('POINT(%s %s)' % (picture['lon'], picture['lat']))
		#event = GEvent('click', 'function() { location.href = "%s"}' % picture['href'])
		#marker.add_event(event)
		#markers.append(marker)
	#return GoogleMap(center=(0,0), zoom=1, markers=markers, key='AIzaSyBI2r_ZwESKtz3jMuwEpVAkzu1M0qeOJAw')

