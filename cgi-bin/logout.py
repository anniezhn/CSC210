#!/usr/bin/python

#Log a user out by expiring his/her cookie, setting session ID to null, link back to home page
import cgi, Cookie, os, cgitb, uuid, sys
import MySQLdb as mdb

#setup
cgitb.enable() #catch Python errors

#get both cookies and set expiration dates in the past
cookie = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
username = cookie['user'].value
cookie['session_id'] = ""
cookie['user'] = ""
cookie['session_id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT' #apparently this is the convention
cookie['user']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
cookie['session_id']['path']="/"
cookie['user']['path']= "/"

print "Content-type: text/html"
print cookie
print
print "<html>"
print "<head><title>You have been logged out, " + username + "!</title><head>"
print "<body>"
print "<h1>You have been logged out, " + username + "-- thanks for visiting!</h1>"
print "<h2>You can visit our home page to log in again: </h2>"
print "<p>Cookie: " + str(cookie['user']) + str(cookie['session_id']) + "</p>"
print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
print "</body>"
print "</html>"

#then update MySQL database to empty session ID: needed?
#cur.execute('update Users set Session_ID="" where Username=%s;',username)
#conn.commit()
#conn.close()
