#!/usr/bin/python
#Script to add a new user to our database after they submit a form
import cgi
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
   #handle duplicate usernames (duplicate first names OK)
   if cur.execute("select UserID from Users where Username = %s", uname) != 0:
      print "<head><title>Username already exists</title></head>"
      print "<h1>Sorry, that username has already been claimed!</h1>"
      print "<p>Please go back and pick another one.</p>"
      print "</body>"
      print "</html"
      sys.exit(1)
   cur.execute("insert into Users (Username, FirstName, Birthdate) values(%s,%s,%s);", (uname, fname, birthday))
   cur.execute("select UserID from Users where Username = %s", (uname))
   userID = int(cur.fetchone()[0]) #fetchone returns tuple and we want just 1st value
   #print "Result of fetchone: " + str(userID)
   cur.execute("insert into Passwords (UserID, Pwd) values(%s,%s);", (userID, pword))
   print "<head><title>Your account has been created!</title></head>"
   print "<body>"
   print "<h1>Success: Account created for %s!</h1>" % (uname)
   print "<p>You can now head back to our home page and log in!</p>"
   print "</body>"
   print "</html>"
except mdb.Error, e: #catch SQL errors (cgitb catches Python errors)
   print "<body>"
   print "Error %d: %s" % (e.args[0], e.args[1])
   print "</body>"
   print "</html>"
   sys.exit(1)
finally: #clean up connection
   if c:
      c.close()
