#!/usr/bin/python

import cgi
import sys
import cgitb
cgitb.enable() #catch Python errors
form = cgi.FieldStorage()

#get username/account information from cookie when enabled
#possibly save progress somehow in database?

print 'Content-type: text/plain'
print
print 'A string variable is any combination of letters or numbers contained within quotes. For example, 'Hello World!' is a string and so is 'abc123'.'
