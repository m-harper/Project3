<script type="text/javascript">
	function initialize()
	{
		//set the default options for the map
		var mapOptions = {
		  center: new google.maps.LatLng({{ center_lat|slugify }},{{ center_lon|slugify }}),
		  zoom: {{ zoom|slugify }} ,
		  mapTypeId: google.maps.MapTypeId.ROADMAP
		};

		//create the map object
		map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);


		//construct all of the map markers and place them in the array
		markers = new Array();
		windows = new Array();
		{% for marker in markers %}
			var mMarker = new google.maps.Marker({
				position: new google.maps.LatLng( {{ marker.lat }} , {{ marker.lon }} ),
				map: map,
				title: "{{ marker.title }}"
			});
			markers.push(mMarker);

			var window = new google.maps.InfoWindow;
			windows.push(window);

			google.maps.event.addListener(
				mMarker,
				"{{ marker.event.trigger }}",
				function ()
				{
					windows[{{forloop.counter0}}].open(map, markers[{{forloop.counter0}}]);
				}
			);

			window.setContent
			(
				"<div>" +
					"<img src={{ marker.data.ThumbNailURL }} alt=\"enable javascript\">" +
					" <a href=\"{{marker.data.href}}\"> {{ marker.title }}</a>" +
					"<br>" +
					{% for item in marker.data.ExifInfo.1 %}
						"{{ item }}" +
					{% endfor %}
				"</div>"
			);


			//set the action events
			//google.maps.event.addListener(mMarker,"{{ marker.event.trigger }}", {{ marker.event.action|safe }} );
		{% endfor %}

	}

	//the user can call to remove all map markers
	function clearMarkers()
	{
		for (var i = 0; i < markers.length; i++)
			markers[i].setMap(null);
		while (markers.length != 0)
			markers.pop();
	}


	google.maps.event.addDomListener(window, 'load', initialize);
</script>
