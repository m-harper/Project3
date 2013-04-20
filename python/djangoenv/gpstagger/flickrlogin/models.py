from django.db import models
from flickrapi import FlickrAPI
from settings import FLICKR_API_KEY, FLICKR_API_SECRET
import xml.etree.ElementTree as xml


# Create your models here.
def get_photos(user_id):
	flickr = FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
	#(token, frob) = flickr.get_token_part_one(perms='write')
	# Gets list of photosets of user in xml
	set = flickr.photosets_getList(user_id)
	xml.dump(set)

