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
cookie_string = os.environ.get('HTTP_COOKIE')
form = cgi.FieldStorage()
username = form['username'].value
password = form['password'].value

if cookie_string: #we have a stored cookie already
	havecookie = '''print 'Content-type: text/html'
	print
	print '<html>'
	print '<body>'
	print '<h1>Test stuff </h1>'
	print '<p>Stored cookie</p>'
	print '</body>'
	print '</html>'
	sys.exit(0)'''
	my_cookie = Cookie.SimpleCookie(cookie_string)
	saved_session_id = my_cookie['session_id'].value
	cur.execute('select * from Users where SessionID=%s;',saved_session_id)
	all_results = cur.fetchall()
	if len(all_results) > 0: #session ID matches up, so same user is logging in. Maybe 'you're already logged in' message?
		saved_name = all_results[0][1]
		if saved_name == username: #same user is trying to log in; welcome them back
			print 'Content-type: text/html'
			print
			print '<html>'
			print "<head><title>You're back!</title></head>"
			print '<body>'
			print '<h1>Welcome back ' + saved_name + '!</h1>'
			print '</body>'
			print '</html>'
		else:
			print 'Content-type: text/html'
			print
			print '<html>'
			print '<head><title>Someone else is logged in!</title></head>'
			print '<body>'
			print "<h1>Hey! You can't do that!</h1>"
			#print '<p> Rresults: ' + str(all_results) + '</p>'
			print '<p>' + saved_name + ' is currently logged in.</p>'
			print '<p>Please log this person out before trying to log in yourself.</p>'
			print '</body>'
			print '</html>'
	else: #wrong session ID! But since we have password don't think this case will be triggered
		print 'Content-type: text/html'
		print
		print '<html>'
		print '<body>'
		print '<h1>Error, wrong session_id! See why this could have happened...</h1>'
		print '</body>'
		print '</html>'

else:
	nocookie = '''print 'Content-type: text/html'
	print
	print '<html>'
	print '<body>'
	print '<h1>Test stuff </h1>'
	print '<p>not stored cookie</p>'
	print '</body>'
	print '</html>'
	sys.exit(0)'''
	cur.execute('select UserID from Users where Username=%s;', username)
	#userID = cur.fetchone()[0]
	if cur.fetchone() is not None: #valid username, now we need to check if passwords match
		userID = cur.fetchone()[0]
		cur.execute('select Pwd from Passwords where UserID=%s', userID)
		stored_password = str(cur.fetchone()[0])
		if password != stored_password: #valid username but wrong associated password
			print 'Content-type: text/html'
			print
			print '<html>'
			print '<head><title>Wrong password!</title></head>'
			print '<body>'
			print "<h1>Sorry, that's the wrong password!</h1>"
			print '<p>Please go back and try again.</p>'
			print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
			print '</body>'
			print '</html>'
		else: #show login page because username and password match
			#print 'condition triggered'
			session_id = str(uuid.uuid4()) #generate secure, random session ID
			cur.execute('update Users set SessionID=%s where UserID=%s',(session_id, userID))
			conn.commit() #call this to commit changes to MySQL database
			cook1 = Cookie.SimpleCookie()
			cook1['session_id'] = session_id
			cook1['session_id']['expires']=24*60*60  #set cookie to expire in a day
			cook2 = Cookie.SimpleCookie()
			cook2['user'] = username
			cook2['user']['expires']=24*60*60
			print 'Content-type: text/html'
			print cook1 #send the cookies (Python takes care of format) to browser
			print cook2
			print # don't forget newline
			print '<html>'
			print '<head><title>You have been logged in!</title></head>'
			print '<body>'
			print '<h1>Hello, ' + username + ", You're now logged in.</h1>"
			print '<p><a href="http://tnichols.rochestercs.org/homepage.html">Click here to start or continue learning!</a></p>'
			print '<p>Enjoy the site!</p>'
			print '</body>'
			print '</html>'
	else: #that username doesn't exist at all!
		print 'Content-type: text/html'
		print # don't forget newline
		print '<html>'
		print '<head><title>Error: unregistered user</title></head>'
		print '<body>'
		print '<h1>Sorry, you seem to be an unregistered user.</h1>'
		print '<p>Please head back to our home page to register for an account!</p>'
		print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
		print '</body>'
		print '</html>'
