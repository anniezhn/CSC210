#!/usr/bin/python

import cgi
import sys
import cgitb
cgitb.enable() #catch Python errors
form = cgi.FieldStorage()

#get username/account information from cookie when enabled
#possibly save progress somehow in database?

print "Content-type: text/html"
print #don't forget the extra newline!
print "<html>"

print "<head><title>TAJ: Basics 1 </title></head>"
print "<body>"
print "<h1>First Lesson: </h1>"
print "<h2>Definitions: </h2>"
print "<p><strong>Variables:</strong> </p>"
print "</body>"
print "</html>"
