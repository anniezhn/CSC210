#!/usr/bin/python

import cgi, Cookie, os, cgitb, uuid, sys
import MySQLdb as mdb

# possibilities
# -- same user logs in again
# -- someone else tries to log in while another user logged in (maybe)?
# --log in for first time: correct and incorrect password, nonexistent username
# --logout: we set the cookie's expiration date to sometime in the past and session ID equal to null

#setup
cgitb.enable() #catch Python errors
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210') #connect to MySQL
cur = conn.cursor()

#look at cookie we currently have...if we have one
form = cgi.FieldStorage()
username = form['username'].value
password = form['password'].value

cur.execute('select UserID from Users where Username=%s;', username)
result = cur.fetchone()
if result is not None: #valid username, now we need to check if passwords match
	userID = result[0]
	cur.execute('select Pwd from Passwords where UserID=%s', userID)
	stored_password = str(cur.fetchone()[0])
	#stored_password = 'password'
	if password != stored_password: #valid username but wrong associated password
		print 'Content-type: application/json'
		print
		print '{"username": "foobar", "password": null}'
	else: #show login page because username and password match
		#print 'condition triggered'
		session_id = str(uuid.uuid4()) #generate secure, random session ID
		cur.execute('update Users set SessionID=%s where UserID=%s',(session_id, userID))
		conn.commit() #call this to commit changes to MySQL database
		cook1 = Cookie.SimpleCookie()
		cook1['session_id'] = session_id
		cook1['session_id']['expires']=24*60*60  #set cookie to expire in a day
		cook1['session_id']['path']='/'
		cook2 = Cookie.SimpleCookie()
		cook2['user'] = username
		cook2['user']['expires']=24*60*60
		cook2['user']['path']='/'
		print 'Content-type: application/json'
		print
		print '{"username": "' + username + '", "password": "foobar", "path": "/", "session_id": "' + session_id + '"}'
		#print cook1.js_output(), cook2.js_output()
else: #that username doesn't exist at all!
	print 'Content-type: application/json'
	print # don't forget newline
	print '{"username": null, "password": "foobar"}'
