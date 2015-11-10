#!/usr/local/bin/python3.3
'''This script makes the .csv for the random .onion domains plot'''
#(4) Content-category histogram for the random domains
#	figure: bar charts

import csv
from pprint import pprint
from cats import Hs as CATs


#rand_domains = open('logs/RANDOM_DOMAINS.txt').readlines()
#rand_domains = [ x.strip() for x in rand_domains ]

rand_domains = CATs.keys()

founds = [ x for x in rand_domains if x in CATs ]


this_cats = [ (CATs[x])[0] for x in founds ]
this_allcats = []
for x in founds:
	this_allcats.extend( CATs[x] )


z = [ (x,this_cats.count(x)) for x in set(this_cats) if x != 'skip' ]
z2 = [ (x,this_allcats.count(x)) for x in set(this_allcats) if x != 'skip' ]

#pprint(allhist)


    
with open("fig4.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(z2)

    print( "Wrote %d domains in %d categories to fig4.csv" % ( len(rand_domains), len(z2) ) )


