#!/usr/bin/python

#Log a user out by expiring his/her cookie, setting session ID to null, link back to home page
import cgi, Cookie, os, cgitb, uuid, sys
import MySQLdb as mdb

print "Content-type: text/html"
print
print "<head><title>You have been logged out!</title><head>"
print "<h1>You have been logged out -- thanks for visiting!</h1>"
print "<h2>You can visit our home page to log in again: </h2>"
print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
print "</body>"
print "</html>"

#get cookie and set its expiration date in the past
cookie = Cookie.SimpleCookie()
cookie['session_id'] = ""
cookie['session_id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT' #apparently this is the convention

#then update MySQL database to empty session ID: needed?
update Users set Session_ID="" where