#!/usr/local/bin/python3.3


from pprint import pprint
from cats import Hs as CATs



lines = open('11-1-out-final.log').readlines()

lines = [ x.strip() for x in lines ]

z = sorted(random.sample(lines,200))

dupes = [ x for x in z if x in CATs ]

for x in dupes:
	print("old: http://%s.onion" % x )

new = [ x for x in z if x not in CATs ]

for x in new:
	print( 'http://' + x + '.onion')

