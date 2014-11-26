#!/usr/bin/python

import cgi
import sys
import cgitb
import MyQSQLdb as mdb

#catch Python errors
cgitb.enable() 

# Connect Python and MySQL
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

# Get username from cookie
cookie = os.environ.get('HTTP_COOKIE')
# Get score from POST
score = form['score'].value

username = cookie['user']
try:
	if cur.execute('select UserID from Users where Username=%s;', username) != 0:
 		cur.execute("select UserID from Users where Username=%s", (uname))
   		userID = int(cur.fetchone()[0]) #fetchone returns tuple and we want just 1st value
   		if cur.execute("select Quiz1 (UserID, Quiz1) values(%s,%s)", (UserID, score)) != null:
   			print 'Content-type: text/html'
   			print
   			print '<html>'
   			print '<body>'
   			print 
		cur.execute("insert into Quiz1 (UserID, Quiz1) values(%s,%s);", (UserID, score))

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