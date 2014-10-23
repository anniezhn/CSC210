#!/usr/bin/python

#need to add MySQL session ID field -- Done by Tom
import cgi, Cookie, os, cgitb, uuid, sys
import MySQLdb as mdb

# possibilities
# -- same user logs in again
# -- someone else tries to log in while another user logged in (maybe)?
# --log in for first time: correct and incorrect password, nonexistent username
# --logout: we set the cookie's expiration date to sometime in the past and session ID equal to null

#setup
cgitb.enable() #catch Python errors
conn = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210'); #connect to MySQL
cur = conn.cursor()

#look at cookie we currently have
cookie_string = os.environ.get('HTTP_COOKIE')

print "Content-type: text/html"

if cookie_string: #we have a stored cookie already
    my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['session_id'].value
    cur.execute('select * from Users where SessionID=%s;',saved_session_id)
    all_results = cur.fetchall()
    if len(all_results) > 0: #session ID matches up, so same user is logging in. Maybe "you're already logged in" message?
        saved_name = all_results[0][0]
		print
        print "<html>"
        print "<body>"
		print "<head><title>You're back!</title></head>"
        print "<h1>Welcome back " + saved_name + "</h1>"
        print "</body>"
        print "</html>"
    else: #wrong session ID! But since we have password not sure if this case will be triggered
	    print
        print "<html>"
        print "<body>"
        print "<h1>Error imposter wrong session_id</h1>"
        print "</body>"
        print "</html>"

else: #have no cookie yet, so user must be trying to log in.
    form = cgi.FieldStorage()
    username = form['username'].value
    password = form['password'].value
    # check whether username exists in MySQL database, whether passwords match up...
	#part of this copied over from login.py -- this will be the new login.py later
	#also: might want to have the homepage only have a signup form and have a link to another
	#html page with a login form, or vice versa -- would simplify things
    c.execute('select UserID from Users where Username=%s;', username)
    userID = cur.fetchone()[0]
    if len(userID) > 0: #valid username, now we need to check if passwords match
	    cur.execute("select Pwd from Passwords where UserID=%s", userID)
        stored_password = str(cur.fetchone()[0])
		if password != stored_password: #valid username but wrong associated password
		    print "<html>"
            print "<head><title>Wrong password!</title></head>"
            print "<body>"
            print "<h1>Sorry, that's the wrong password!</h1>"
            print "<p>Please go back and try again.</p>"
			print "<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>"
            print "</body>"
            print "</html>"
        else: #show login page because username and password match
            session_id = str(uuid.uuid4()) #generate secure, random session ID
            cur.execute('update Users set SessionID=? where UserID=?',
                  (session_id, userID))
            conn.commit() #call this to commit changes to MySQL database
            cook = Cookie.SimpleCookie()
            cook['session_id'] = session_id
            print cook #send the cookie (Python takes care of format) to browser
            print # don't forget newline
            print "<html>"
            print "<body>"
			print "<head><title>You have been logged in!</title></head>"
            print "<h1>Hello, " + username + ", You're now logged in.</h1>"
            print "<p>Enjoy the site!</p>"
            print "</body>"
            print "</html>"
    else: #that username doesn't exist at all!
        print # don't forget newline
        print "<html>"
		print "<head><title>Error: unregistered user</title></head>"
        print "<body>"
        print "<h1>Sorry, you seem to be an unregistered user.</h1>"
		print "<p>Please head back to our home page to register for an account!</p>"
		print "<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>"
        print "</body>"
        print "</html>"

