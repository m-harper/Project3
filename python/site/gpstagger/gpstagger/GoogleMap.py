from django.utils.html import format_html
from django.template.loader import render_to_string

class GoogleMapException(Exception):
	pass

GOOGLE_MAPS_URL='https://maps.googleapis.com/maps/api/js?key='

class GoogleMap:

	def __init__(self, markers=[], center=(0, 0), zoom=4, key=None, sensor='false'):
		self.markers = markers
		self.center = center
		self.zoom = zoom
		self.key = key
		self.sensor = sensor
		self.dom_id = 'map'

		self.template = 'GoogleMapTemplate.js'
		self.api_url = GOOGLE_MAPS_URL

		self.strCenter = str(center)
		self.strZoom = str(zoom)

	# access the google Map API
	@property
	def api_script(self):
		return format_html('<script src="{0}{1}&sensor={2}" type="text/javascript"></script>', self.api_url, self.key, self.sensor)

	#display the Map and Markers
	def render(self):
		params = {
				  'center_lat' : self.center[0],
				  'center_lon' : self.center[1],
				  'dom_id' : self.dom_id,
				  #'js_module' : self.js_module,
				  'zoom' : self.zoom,
				  'markers' : self.markers,
				  }
		return render_to_string(self.template, params)

	#@property
	#def onload(self, ):
	#	return format_html('onload="{0}.{1}_load()"', self.js_module, self.dom_id)

	@property
	def body(self):
		return format_html('<div id="map-canvas"/>')

	@property
	def onunload(self):
		return format_html('onunload="GUnload()"')

class GEvent:
	def __init__(self, trigger='click', action='function(){}'):
		self.trigger = trigger
		self.action = action

class GMarker:
	def __init__(self, lat, lon, title=None, event=None):
		self.lat = lat
		self.lon = lon
		self.title = title

		if event is None: self.event = event

	def add_event(self, event ):
		self.event = event
