#!/usr/bin/python

import cgitb, cgi, os, Cookie, sys
import MySQLdb as mdb

#setup
cgitb.enable()
#retrieve username from cookie
cookie_monster = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
username = cookie_monster['user'].value

conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

#expire all cookies
cookie_monster['session_id'] = ""
cookie_monster['user'] = ""
cookie_monster['session_id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT' #apparently this is the convention
cookie_monster['user']['expires']='Thu, 01 Jan 1970 00:00:00 GMT' #apparently this is the convention

#remove user from database
cur.execute('SELECT UserID FROM Users WHERE Username=%s;', username)
userID = cur.fetchone()[0]
cur.execute("DELETE FROM Users WHERE Username=%s",username)
conn.commit()
cur.execute("DELETE FROM Passwords WHERE UserID=%s",userID)
conn.commit()

print "Content-type: text/html"
print cookie_monster
print
print "<html>"
print "<head><title>Your account has been deleted</title></head>"
print "<body>"
print "<h1>OK, " + username + ", your account has been deleted. Thank you for using our site.</h1>"
print "<p>Click here to go back to our homepage:</p>"
print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
print "</body>"
print "</html>"

