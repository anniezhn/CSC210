#!/usr/bin/python

#Check if there is a cookie, which indicates the user is logged in
import cgi, Cookie, os, cgitb, sys

#failedAttempt = print "Hello!"
#sys.exit(0)
cookie = os.environ.get('HTTP_COOKIE')
if cookie: #redirect
	print 'Content-type: text/plain'
	print
	print "http://tnichols.rochestercs.org/homepage.html"
	print

'''def main(): #return True if there's a cookie and false if not
	#print "Hey there!"
	if 'HTTP_COOKIE' in os.environ:
		print "COOKIE"
		sys.exit(0) #if this does not work, substitute "return True"
	else:
		print "NO COOKIE"
		sys.exit(1) #if this does not work, substitute "return False"

if __name__ == "__main__":
	main()'''

'''print "Content-type: text/plain"
print #remember the blank line
if 'HTTP_COOKIE' in os.environ:
	print "true"
else:
	print "false"'''
