#!/usr/bin/python
#Script to add a new user to our database after they submit a form
#Update 11/1: User is auto-logged in after they create account
import cgi, Cookie, uuid
import MySQLdb as mdb
import sys
import cgitb

cgitb.enable() #catch Python errors
form = cgi.FieldStorage()

#get user input from form
uname = form['username'].value 
pword = form['password'].value #same thing:
fname = form['fname'].value
month = form['month'].value
day = form['day'].value
year = form['year'].value

#connect Python and MySQL
c = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210');
cur = c.cursor()
birthday = str(year) + '-' + str(month) + '-' + str(day) #convert into MySQL's date format

try:
   #handle duplicate usernames (duplicate first names OK)
   if cur.execute("select UserID from Users where Username = %s", uname) != 0:
      print "Content-type: text/html"
      print
      print "<html>"
      print "<head><title>Username already exists</title></head>"
      print '<body>'
      print "<h1>Sorry, that username has already been claimed!</h1>"
      print "<p>Please go back and pick another one.</p>"
      print '<p><a href="http://tnichols.rochestercs.org">Home Page</a></p>'
      print "</body>"
      print "</html"
      sys.exit(1)
   #add relevant user and password info into corresponding tables in database
   cur.execute("insert into Users (Username, FirstName, Birthdate) values(%s,%s,%s);", (uname, fname, birthday))
   cur.execute("select UserID from Users where Username=%s", (uname))
   userID = int(cur.fetchone()[0]) #fetchone returns tuple and we want just 1st value
   cur.execute("insert into Passwords (UserID, Pwd) values(%s,%s);", (userID, pword))

   #log user in automatically
   session_id = str(uuid.uuid4()) #generate secure, random session ID
   cur.execute('update Users set SessionID=%s where UserID=%s',(session_id, userID))
   c.commit() #call this to commit changes to MySQL database
   cook1 = Cookie.SimpleCookie()
   cook1['session_id'] = session_id
   cook1['session_id']['expires']=24*60*60  #set cookie to expire in a day
   cook1['session_id']['path']='/'  #set cookie to expire in a day
   cook2 = Cookie.SimpleCookie()
   cook2['user'] = uname
   cook2['user']['expires']=24*60*60
   cook2['user']['path']='/'

   print 'Content-type: text/html'
   print cook1
   print cook2
   print # don't forget newline
   print '<html>'
   print "<head><title>Your account has been created!</title></head>"
   print '<body>'
   print "<h1>Success: Account created for %s!</h1>" % (uname)
   print '<p><a href="http://tnichols.rochestercs.org/homepage.html">Click here to start or continue learning!</a></p>'
   print '<p>Enjoy the site!</p>'
   print "</body>"
   print "</html>"
except mdb.Error, e: #catch SQL errors (cgitb catches Python errors
   print 'Content-type: text/html'
   print # don't forget newline
   print '<html>'
   print "<body>"
   print "Error %d: %s" % (e.args[0], e.args[1])
   print "</body>"
   print "</html>"
   sys.exit(1)
finally: #clean up connection
   if c:
      c.close()
