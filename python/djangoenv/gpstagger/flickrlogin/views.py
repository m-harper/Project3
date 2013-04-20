from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from settings import FLICKR_API_KEY, FLICKR_API_SECRET
import flickrapi

def index(request):
	if 'flickr_token' in request.session:
		token = True
	else:
		flickr = flickrapi.FlickrAPI(
			FLICKR_API_KEY, 
			FLICKR_API_SECRET)
		flickr.get_token_part_one(
			perms='write')	
		token = False
	
	context = {
		'token': token
		}
	return render_to_response(
			'index.html',
			context,
			context_instance=RequestContext(request))

def flickr_callback(request):
	if not 'flickr_token' in request.session:
		f = flickrapi.FlickrAPI(
			FLICKR_API_KEY, 
			FLICKR_API_SECRET, 
			store_token=False)
		frob = None
		token = None	
		try:
			frob = request.GET['frob']
			token = f.get_token(frob)
			request.session['flickr_token'] = token		
		except Exception:
			pass

	return redirect('index')
