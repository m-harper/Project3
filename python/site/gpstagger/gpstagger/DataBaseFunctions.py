import sqlite3
import json

def addPicture( picture ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	c.execute('INSERT INTO picturesTable VALUES (?,?)', [ picture['name'], json.dumps( picture, sort_keys=True, indent=1), ] )
	conn.commit()
	return

def removePicture( pictureName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	c.execute('DELETE FROM picturesTable WHERE name = ?', pictureName )
	conn.commit()
	return

def getPictureJSON( pictureName):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	c.execute("SELECT json FROM picturesTable WHERE name = ?", pictureName)
	return c.fetchall()[0][0]

def getPicture( pictureName ):
	pictureJSON = getPictureJSON( pictureName )
	return json.loads(pictureJSON)

def getPicturesJSON():
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	c.execute("SELECT json FROM picturesTable")
	return c.fetchall()

def getPictures( ):
	picturesJSON = getPicturesJSON()
	picturesPYTHON = []
	for x in range(0,len(picturesJSON)):
		picturesPYTHON.append(json.loads(picturesJSON[x][0]))
	return picturesPYTHON

def resetDB():
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	c.execute("DROP TABLE picturesTable ")
	c.execute("CREATE TABLE picturesTable (name, json)")
	conn.commit()
	return

	#tables in database
	#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	#print(c.fetchall())
