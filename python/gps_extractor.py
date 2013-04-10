from EXIF import *

def get_gps(filename):
	file = open(filename)
	data = process_file(file)
	coords = []
	
	for tag in data.keys():
		if 'GPSLatitude' in tag or 'GPSLongitude' in tag:
			if not 'Ref' in tag:
				string = str(data[tag])
				
				dindex = string.find(',')
				d = int(string[1:dindex])
				
				string = string[dindex + 2:]
				
				m = int(string[0:string.find(',')])
				
				string = string[string.find(',') + 2:]
				
				num = string[0:string.find('/')]
				denom = string[string.find('/') + 1:string.find(']')]
				
				s = float(num) / float(denom)
				DD = d + float(m)/60 + float(s)/3600
				
				coords.append(DD)
	
	return coords
