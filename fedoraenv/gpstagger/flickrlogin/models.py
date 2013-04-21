from django.db import models
from flickrapi import FlickrAPI as api
from gpstagger.settings import FLICKR_API_KEY as key, FLICKR_API_SECRET as secret

class photo_grabber(models.Model):
	user_name = models.CharField(max_length=50)

	def find_long_index(self, exif):
		for i in range(len(exif[0])):
			if exif[0][i].attrib['label'] == 'GPS Longitude':
				return i

	def find_lat_index(self, exif):
		for i in range(len(exif[0])):
			if exif[0][i].attrib['label'] == 'GPS Latitude':
				return i

	def get_longitude(self, exif):
		return exif[0][self.find_long_index(exif)][0].text

	def get_latitude(self, exif):
		return exif[0][self.find_lat_index(exif)][0].text

	def get_exif(self, photo_id):
		flickr = api(api_key=key, secret=secret)
		exiftree = flickr.photos_getExif(api_key=key, photo_id=photo_id)
		return exiftree
		
	def get_gps(self, photo_id):
		exif = self.get_exif(photo_id)
		latitude = self.get_latitude(exif)
		longitude = self.get_longitude(exif)
		return (latitude, longitude)

	def get_photo_list(self, photoset_id):
		flickr = api(api_key=key, secret=secret)
		phototree = flickr.photosets_getPhotos(api_key=key, photoset_id=photoset_id)

		photolist = []
		for photo in phototree[0]:
			photolist.append(photo.attrib['id'])
		return photolist


	def get_set_list(self, user):
		flickr = api(api_key=key, secret=secret)

		# Convert the username to user id
		user_id_etree = flickr.people_findByUsername(api_key=key, username=user)
		userid = user_id_etree[0].attrib['id']

		# Get the list of photo set ids
		list = []
		sets = flickr.photosets_getList(api_key=key, userid=userid)
		for photoset in sets[0]:
			list.append(photoset.attrib['id'])
		return list

	def get_all_gps(self, username):
		coords = []
		sets = self.get_set_list(username)
		for set in sets:
			photos = self.get_photo_list(set)
			for photo in photos:
				coords.append(self.get_gps(photo))
		return coords

	def __unicode__(self):
		return self.user_name


class test:
	pg = photo_grabber()
	coords = pg.get_all_gps('projecttamu')