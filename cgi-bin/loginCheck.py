#!/usr/bin/python

#Check if there is a cookie, which indicates the user is logged in
import cgi, Cookie, os, cgitb, sys

failedAttempt = '''print "Hello!"
sys.exit(0)
if 'HTTP_COOKIE' in os.environ: #redirect
	#print 'Content-type: text/html'
	print "Location: http://tnichols.rochestercs.org/homepage.html"
	print'''

def main(): #return True if there's a cookie and false if not
	#print "Hey there!"
	if 'HTTP_COOKIE' in os.environ:
		print "COOKIE"
		sys.exit(0) #if this does not work, substitute "return True"
	else:
		print "NO COOKIE"
		sys.exit(1) #if this does not work, substitute "return False"

if __name__ == "__main__":
	main()
