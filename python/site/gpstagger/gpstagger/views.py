#needed for all views
from django.http import HttpResponse

#template function
from django.shortcuts import render_to_response

from django.contrib.auth import logout

#google map django bindings
#from django.contrib.gis.maps.google.gmap import GoogleMap
#from django.contrib.gis.maps.google.overlays import GMarker, GEvent
from GoogleMap import GoogleMap, GMarker, GEvent

#database types
from gpstagger.models import picture, make_picture

#used for DB actions
import DataBaseFunctions as DBF

#from flickrlogin.models import photo_grabber


#views receives some HttpResponse and returns an HttpResponse
def hello(request):
	return HttpResponse("Hello world")

def index(request):	
	name = request.GET.get('name')	
	print name
	request.session['userName'] = name
	return render_to_response('index.html')
	
def hello(request):
	return HttpResponse("Hello world")

def importPhotosfunc(request):
	#pg=photo_grabber
	#coords = get_all_gps(uname)
	#for coord in coords:
	#	DBF.addPicture( make_picture( 'default_', coord[0], coord[1], 'http://127.0.0.1:8000/hello/'), request['userName'] )
	return HttpResponse("Hello world")


def gmapfunc(request):
	#get Current User
	userName = request.session['userName']

	#get all the pictures fromt the DataBase (as Python Objects)
	pictures = DBF.getPictures(userName)

	#create the Map
	gmap = createGoogleMap( pictures )

	return render_to_response('map.html', {'gmap':gmap,})

def mapTest(request):
	#spoof session
	request.session['userName'] = 'fIFO'
	userName = request.session['userName']

	#add the new user and a couple photos
	DBF.addUser(userName)
	DBF.addPicture( make_picture( 'default_', "0", "0", 'http://127.0.0.1:8000/hello/'), userName )
	DBF.addPicture( make_picture( 'default_', "-10", "-10", 'http://127.0.0.1:8000/hello/'), userName )
	DBF.addPicture( make_picture( 'default_', "10", "10", 'http://127.0.0.1:8000/hello/'), userName )
	DBF.addPicture( make_picture( 'default_', "10", "-10", 'http://127.0.0.1:8000/hello/'), userName )
	DBF.addPicture( make_picture( 'default_', "-10", "10", 'http://127.0.0.1:8000/hello/'), userName )


	#get all the user's pictures
	pictures = DBF.getPictures(userName)

	#create the Map
	gmap = createGoogleMap( pictures )

	#remove phony user
	DBF.removeUser(userName)
	logout(request)

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

