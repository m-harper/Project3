#needed for all views
from django.http import HttpResponse

#template function
from django.shortcuts import render_to_response, redirect

#logout user function
from django.contrib.auth import logout

#google map django bindings
from GoogleMap import GoogleMap, GMarker, GEvent

#database types
from gpstagger.models import picture, make_picture

#used for DB actions
import DataBaseFunctions as DBF

#exif data parser/fetcher
from flickrlogin.models import photo_grabber

invalidUserName = 0


################
#VIEW FuNCTIONS#
################

#views receives some HttpResponse and returns an HttpResponse
def hello(request):
	return HttpResponse("Hello world")


#logout the current user
def logout(request):
	return redirect('/')


#remove user from the database
def deleteuser(request):
	userName = request.session['userName']
	DBF.removeUser(userName)
	return redirect('/')

#the main login page
def index(request):
	global invalidUserName
	name = request.GET.get('name')
	print name
	if name is not None:
		request.session['userName'] = name
		return redirect('/importPhotos')
	if invalidUserName == 0:
		return render_to_response('index.html')
	else:
		return render_to_response('indexerror.html')


#parse all the user's photos and the exif data, pass to map
def importPhotos(request):
	global invalidUserName
	pg = photo_grabber()

	#fetch all the user's photos
	try:
		photos = pg.get_all_photos( request.session['userName'] )
	except:
		print "Invalid UserName!"
		invalidUserName = 1
		return redirect('/')
	invalidUserName = 0

	#add the user to the databse
	DBF.addUser( request.session['userName'] )

	#positioning data for non-gps tagged photos
	LONGITUDE = -30
	SEPARATOR_SPACE = 110 / len(photos)
	count = 0
	index = 0;

	#set photo marker data
	for photo in photos:
		print photo
		title = photo['title']
		lat = (photo['gps'])[1]
		lon = (photo['gps'])[0]
		#if the photo does not have gps data, place it in the mid-atlantic
		if lat == 0 and lon == 0:
			lat = LONGITUDE
			lon = -65 + SEPARATOR_SPACE * count
			count = count + 1
		href = photo['href']
		#uncomment the line below and comment the one below that for exif parsing fun
		#exifData = photo['exifTree']
		exifData = ['exifTree']
		DBF.addPicture( make_picture( title, lat, lon, href, exifData ), request.session['userName'] )
	return redirect('/map')


def gmapfunc(request):
	#get Current User
	userName = request.session['userName']

	#get all the pictures fromt the DataBase (as Python Objects)
	pictures = DBF.getPictures(userName)

	#print "PICTURES: {}".format(pictures)

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


###################
#UTILITY FUNCTIONS#
###################


#non-django GoogleMap v3 implementation. made to imitate django gis v2 version
def createGoogleMap( pictures ):
	markers = []
	# create a marker for each picture
	for picture in pictures:
		marker = GMarker(picture['lon'], picture['lat'], picture['name'])
		#event = GEvent('click', 'function() { location.href = "%s"}' % picture['href'])
		event = GEvent('click')
		endURLindex = picture['href'].rfind('.', 0, len(picture['href']))
		ThumbNailUrl = picture['href'][:endURLindex] + '_t' + picture['href'][endURLindex:]
		marker.data['ThumbNailURL'] = ThumbNailUrl
		marker.data['ExifInfo'] = picture['exifData']
		marker.data['href'] = picture['href']
		marker.add_event(event)
		markers.append(marker)
	#generate and return the map object
	return GoogleMap(center=(0,0), zoom=3, markers=markers, key='AIzaSyBI2r_ZwESKtz3jMuwEpVAkzu1M0qeOJAw')

