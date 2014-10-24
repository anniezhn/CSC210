#!/usr/bin/python

import cgi
import sys
import cgitb
cgitb.enable() #catch Python errors
form = cgi.FieldStorage()

#get username/account information from cookie when enabled
#possibly save progress somehow in database?
