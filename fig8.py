#!/usr/local/bin/python3.3

import json, codecs, sys, csv
from pprint import pprint
import geoip2.database
import geoip2.webservice

DB_FNAME = '/g/darkwebpaper/logs/GeoIP2-Domain.mmdb'
db = geoip2.database.Reader( DB_FNAME )

user_id = 42
license_key = None
client = geoip2.webservice.Client( user_id, license_key )

ips = None
with open('logs/owned_ips.log') as f:
	ips = [ x.strip() for x in f.readlines() ]

#pprint(ips)

for ip in ips:
	r1 = db.domain( ip )
	print( "domain=%s" % (r1.domain) )
#r2 = client.city('128.101.101.101')


#print( r1 )

#print( r2.location.latitude )
#print( r2.location.longitude )

db.close()
