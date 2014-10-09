#!/usr/bin/python

#TODO: Actually take this info that we have and add user to database
# use cookies for persistent login

import cgi
import datetime

# to facilitate debugging
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-type: text/html"
# don't forget the extra newline!
print

print "<html>"
print "<head><title>Your account has been created!</title></head>"
print "<body>"
print "<h1>Welcome to our site, " + form['fname'].value + "</h1>"
#print "<p>The time is: " + str(datetime.datetime.now()) + "</p>"
print "<h2>Here is the information we have on record:</h2>"
print "<p>Your username is: " + form['username'].value + "</p>"
print "<p>Your password is: " + form['password'].value + "</p>"
print "<p> Your birthday is: " + form['month'].value + " " + form['day'].value + " </p>"
print "<p> Remember to log out when you're done with the website! </p>"
print "</body>"
print "</html>"
