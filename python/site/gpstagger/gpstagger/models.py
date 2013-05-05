from django.db import models


class picture(models.Model):
	json = models.TextField()

	def __unicode__(self):
		return unicode(self.json)

def make_picture(name, lat, lon, href, exifData):
	dictionary = { 'name':'name', 'lat': 'lat', 'lon': 'lon', 'href': 'href', 'exifData': 'exifData', }
	dictionary['name'] = name
	dictionary['lat'] = lat
	dictionary['lon'] = lon
	dictionary['href'] = href
	dictionary['exifData'] = exifData
	return dictionary
