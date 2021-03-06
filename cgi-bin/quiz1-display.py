#!/usr/bin/python

import cgi
import sys
import cgitb
import MyQSQLdb as mdb

#catch Python errors
cgitb.enable() 

# Connect Python and MySQL
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

# Get username from cookie
cookie = os.environ.get('HTTP_COOKIE')

username = cookie['user']
cur.execute('select UserID from Users where Username=%s;', username)
result = cur.fetchone()

if result is not None: # The username exists (which it should! but just to be sure)
	userID = result[0]
   	cur.execute('select Score1 from Quiz1 where UserID=%s',userID)
	score1 = str(cur.fetchone()[0])
	if score1 != Null: #if there is a quiz grade in the database.
		print 'Content-type: text/plain'
		print
		print "You have already taken Quiz 1 and received" + score1 + ""
	else:
		print 'Content-type: text/plain'
		print
		print "You have not passed the first lesson yet"
else: # username doesn't exist
	print 'Content-type: text/plain'
	print
	print 'You do have have a valid username!"

conn.close()