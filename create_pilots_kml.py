#!/usr/bin/python
#
# TODO: I don't remember what this script was for, probably it was for
# creating a KML file with paragliding pilots addresses.

import sys
import MySQLdb

print 'Test'
db= connect(host="192.168.1.2", user="mc303" , passwd="mysql234", db="address")
cursor= db.cursor()
sys.exit(0)
