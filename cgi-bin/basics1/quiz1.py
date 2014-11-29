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
score = Request.Form("score1")

username = cookie['user']
cur.execute('select UserID from Users where Username=%s;', username)
result = cur.fetchone()
try:
	if result is not None:
		userID = result[0]
		cur.execute('select Score1 from Quiz1 where UserID=%s',userID)
		score1 = str(cur.fetchone()[0])
			if score1 != Null:
				cur.execute('update Users set Quiz1=%s where UserID=%s',(score, userID))
				conn.commit()
			else:
				cur.execute("insert into Quiz1 (UserID, Quiz1) values(%s,%s);", (UserID, score))
				conn.commit()
	else:
		sys.exit(1)

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