#!/usr/bin/python
#test: connect to our mySQL database, insert a user
import cgi
import MySQLdb as mdb
import sys
import cgitb

cgitb.enable() #catch errors
form = cgi.FieldStorage()

#get user input from form
uname = form['username'].value 
pword = form['password'].value #same thing:
fname = form['fname'].value
month = form['month'].value
day = form['day'].value
year = form['year'].value
   #c = mdb.connect('localhost', 'tnichol1_webuser', 'Ad%2a#Dac9q', 'tnichol1_CSC210'); currently not working with new user...weird
c = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210');
cur = c.cursor()
birthday = str(year) + '-' + str(month) + '-' + str(day) #convert into database's format
print "Content-type: text/html"
print
print "<html>"
comout = '''
print "<head><title>Your account has been created!</title></head>"
print "<body>"
print "<h1>Success: Account created for you!</h1>"
print "<p>Remember to log out when you're done!</p>"
print "</body>"
print "</html>"
sys.exit(0)'''
try:
   cur.execute("insert into Users (Username, FirstName, Birthdate) values(%s,%s,%s);", (uname, fname, birthday))
   #how to get UID from inserted user?
   cur.execute("select UserID from Users where Username = %s", (uname))
   userID = cur.fetchone()
   cur.execute("insert into Passwords (UserID, Pwd) values(%s,%s);", (userID, pword))
   print "<head><title>Your account has been created!</title></head>"
   print "<body>"
   print "<h1>Success: Account created for %s!</h1>" % (uname)
   print "<p>Remember to log out when you're done!</p>"
   print "</body>"
   print "</html>"
except mdb.Error, e: #catch SQL errors (cgitb catches Python erros)
   print "<body>"
   print "Date: " + birthday
   print "Error %d: %s" % (e.args[0], e.args[1])
   print "</body>"
   print "</html>"
   sys.exit(1)
finally:
   if c:
      c.close()
