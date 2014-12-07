#!/usr/bin/python

import cgi, Cookie, os, cgitb, sys
import MySQLdb as mdb

#setup
cgitb.enable() #catch Python errors
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

form = cgi.FieldStorage()
username = form['username'].value

cur.execute('select FirstName from Users where Username=%s;', username)
result = cur.fetchone()

if result is not None:
  print 'Content-type: text/plain'
  print # don't forget newline
  print str(result)
else
  print 'Content-type: text/plain'
  print # don't forget newline
  print str(username)
