#!/usr/bin/python

import cgi
import MySQLdb as mdb
import sys
import cgitb
cgitb.enable() #catch Python errors

#connect Python and mySQL
c = mdb.connect('localhost', 'tnichol1', 'TeamTAJ2!', 'tnichol1_CSC210');
cur = c.cursor()
