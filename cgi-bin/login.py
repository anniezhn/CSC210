#!/usr/bin/python

import cgi
import MySQLdb as mdb
import sys
import cgitb
cgitb.enable() #catch Python errors
form = cgi.FieldStorage()

#TODO: Use cookies for persistent login
username = form['username'].value
password = form['password'].value

#connect Python and mySQL
c = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210');
cur = c.cursor()

print "Content-type: text/html"
# don't forget the extra newline!
print
print "<html>"

#retrieve correct password for user
userID = cur.execute("select UserID from Users where Username=%s", username)
cur.execute("select Pwd from Passwords where UserID=%s", userID)
stored_password = str(cur.fetchone()[0])
if password != stored_password: #error message
  print "<head><title>Wrong password!</title></head>"
  print "<body>"
  print "<h1>Sorry, that's the wrong password!</h1>"
  print "<p>Please go back and try again.</p>"
else: #show login page
  print "<head><title>You have been logged in!</title></head>"
  print "<body>"
  print "<h1>You're now logged in, %s!</h1>" % (username)
  print "<p>Enjoy the site!</p>"
print "<body>"
print "</body>"
print "</html>"
