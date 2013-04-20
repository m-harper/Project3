from django.db import models

#Save to and load from DB
#	https://docs.djangoproject.com/en/dev/topics/serialization/
#DQ Queries
#	https://docs.djangoproject.com/en/dev/topics/db/queries/
#Saving as JSON
#	https://docs.djangoproject.com/en/dev/topics/serialization/#id1
#SQL data Types supported
#	https://docs.djangoproject.com/en/dev/topics/db/models/

# table is not created automatically? why?
#drop table gpstagger_picture;
#sqlite> create table gpstagger_picture(id, name, json);


class picture(models.Model):
	json = models.TextField()

	def __unicode__(self):
		return unicode(self.json)

def make_picture(name, lat, lon, href):
	dictionary = { 'name':'name', 'lat': 'lat', 'lon': 'lon', 'href': 'href', }
	dictionary['name'] = name
	dictionary['lat'] = lat
	dictionary['lon'] = lon
	dictionary['href'] = href
	return dictionary
	#return { 'name': name, 'lat': lat, 'lon': lon, 'href': 'http://127.0.0.1:8000/hello/', }
