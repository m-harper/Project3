import sqlite3
import json

#turn the given picture into a JSON representation and store it, by username, in a table
def addPicture( picture, userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'INSERT INTO {} VALUES (?,?)'.format(userName)
	c.execute(string, [ picture['name'], json.dumps( picture, sort_keys=True, indent=1), ] )
	conn.commit()
	return

#remove the given picture by name for the given user
def removePicture( pictureName, userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'DELETE FROM {} WHERE name = ?'.format(userName)
	c.execute( string , [pictureName] )
	conn.commit()
	return

#retrieve from the database the specified user's picture by the given name
def getPictureJSON( pictureName, userName):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'SELECT json FROM {} WHERE name = ?'.format(userName)
	c.execute(string, [pictureName])
	return c.fetchall()[0][0]

#return the python representation of the specified user's photo
def getPicture( pictureName, userName ):
	pictureJSON = getPictureJSON( pictureName, userName )
	return json.loads(pictureJSON)

#get all pictures for a user and return as JSON strings
def getPicturesJSON( userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'SELECT json FROM {}'.format(userName)
	print string
	c.execute(string)
	return c.fetchall()

#get all pictures for a user and return as python object
def getPictures( userName ):
	picturesJSON = getPicturesJSON(userName)
	picturesPYTHON = []
	for x in range(0,len(picturesJSON)):
		picturesPYTHON.append(json.loads(picturesJSON[x][0]))
	return picturesPYTHON

#clear the database
def resetDB():
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	#code to drop all tables
	conn.commit()
	return

#add a user to the database, if not already present
def addUser( userName ):
	conn = sqlite3.connect('picture.db')
	c = conn.cursor()
	string = 'CREATE TABLE IF NOT EXISTS {} (name, json)'.format(userName)
	c.execute( string )
	conn.commit()
	return

#remove the specified user from the database, if present
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
