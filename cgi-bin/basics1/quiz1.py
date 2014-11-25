#!/usr/bin/python

import cgi
import sys
import cgitb
import MyQSQLdb as mdb


cgitb.enable() #catch Python errors
# Connect Python and MySQL
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

try:
	

except mbd.Error, e:
	print 'Content-type: text/html'
	print
	print '<html>
	print "<body>"
	print "Error %d: %s" % (e.args[0], e.args[1])
	print "</body>"
	print "</html>"
	sys.exit(1)
finally:
	if conn:
		conn.close()