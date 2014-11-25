#!/usr/bin/python

#Will be called by Ajax 
import cgi, Cookie, os, cgitb, uuid, sys
import MySQLdb as mdb

#setup
cgitb.enable() #catch Python errors
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

#fetch data from Ajax call; also need cookie info
form = cgi.FieldStorage()
oldpass = form['oldpass'].value
newpass = form['newpass'].value
confirmpass = form['confirmpass'].value
cookie = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
username = cookie['user'].value

if newpass != confirmpass: #user's new password/confirmation don't match; let's get this check out of the way first
	print 'Content-type: text/plain'
	print
	sys.stdout.write("nomatch")
else: #access MySQL database and fetch the old user's password
	cur.execute('select UserID from Users where Username=%s;', username)
	userID = cur.fetchone()[0]
	cur.execute('select Pwd from Passwords where UserID=%s', userID)
	stored_password = str(cur.fetchone()[0])
	if stored_password != oldpass: #user didn't type old password correctly
		print 'Content-type: text/plain'
		print
		sys.stdout.write("incorrect")
	else: #we're good. Update user's password and let Ajax call know we've succeeded
		cur.execute('update Passwords set Pwd=%s where UserID=%s',(newpass, userID))
		conn.commit()
		print 'Content-type: text/plain'
		print
		print "Success"
#no matter what happens, close the SQL connection as good practice
conn.close()
