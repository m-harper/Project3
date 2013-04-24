import sqlite3
import json

def addPicture( picture, userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'INSERT INTO {} VALUES (?,?)'.format(userName)
	c.execute(string, [ picture['name'], json.dumps( picture, sort_keys=True, indent=1), ] )
	conn.commit()
	return

def removePicture( pictureName, userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'DELETE FROM {} WHERE name = ?'.format(userName)
	c.execute( string , [pictureName] )
	conn.commit()
	return

def getPictureJSON( pictureName, userName):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'SELECT json FROM {} WHERE name = ?'.format(userName)
	c.execute(string, [pictureName])
	return c.fetchall()[0][0]

def getPicture( pictureName, userName ):
	pictureJSON = getPictureJSON( pictureName, userName )
	return json.loads(pictureJSON)

def getPicturesJSON( userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'SELECT json FROM {}'.format(userName)
	print string
	c.execute(string)
	return c.fetchall()

def getPictures( userName ):
	picturesJSON = getPicturesJSON(userName)
	picturesPYTHON = []
	for x in range(0,len(picturesJSON)):
		picturesPYTHON.append(json.loads(picturesJSON[x][0]))
	return picturesPYTHON

def resetDB():
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	#c.execute("DROP TABLE picturesTable ")
	#c.execute("CREATE TABLE picturesTable (name, json)")
	conn.commit()
	return

def addUser( userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'CREATE TABLE IF NOT EXISTS {} (name, json)'.format(userName)
	c.execute( string )
	conn.commit()
	return

def removeUser( userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'DROP TABLE IF EXISTS {} '.format(userName)
	c.execute(string)
	conn.commit()
	return


	#tables in database
	#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	#print(c.fetchall())
