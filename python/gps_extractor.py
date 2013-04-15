from EXIF import *

def get_gps(filename):
	file = open(filename)
	data = process_file(file)
	coords = []
	
	for tag in data.keys():
		#print tag
		#print data[tag]
		if 'GPSLatitude' in tag or 'GPSLongitude' in tag:
			if not 'Ref' in tag:
				string = str(data[tag])
								
				#sets first to degrees
				first = string[1:string.find(',')]				
				string  = string[string.find(',')+2:]
				
				#sets second to minutes
				second = string[0:string.find(',')]				
				string = string[string.find(',')+2:]
				
				#sets third to seconds
				third = string[0:string.find(']')]				
				
				#checks if degrees has a '/'
				if first.find('/') != -1:
					num = first[0:first.find('/')]					
					denom = first[first.find('/') + 1:]					
					d = float(num) / float(denom)
				else:
					d = int(first)
				
				#checks if minutes has a '/'
				if second.find('/') != -1:
					num = second[0:second.find('/')]					
					denom = second[second.find('/') + 1:]					
					m = float(num) / float(denom)
				else:
					m = int(second)				
				
				#checks if seconds has a '/'
				if third.find('/') != -1:
					num = third[0:third.find('/')]					
					denom = third[third.find('/') + 1:]					
					s = float(num) / float(denom)
				else:
					s = int(third)
					
				DD = d + float(m)/60 + float(s)/3600
				
				#latitude at position 0 then longitude at position 1
				coords.insert(0, DD)
			else:
				hem =  str(data[tag])				
				if hem == "S":
					coords[0] = coords[0] * -1
				if hem == "W":
					coords[1] = coords[1] * -1
					print "here"
	
	return coords
print get_gps("IMG_4692.jpg")