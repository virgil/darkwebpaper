#!/usr/local/bin/python3.3

import json, codecs, sys, csv, copy
from pprint import pprint

from cats import Hs as CATs



fname = 'logs/aggregate-oct-nov.json'


#reqs, traffics, h2ips = {}, {}, {}
#Hs_unlabeled_reqs = {}

obj = None
with codecs.open(fname, encoding='utf-8') as f:
    obj = json.load(f)

#Get all of the domains in obj that have a category
obj = { key:value for key,value in obj.items() if key in CATs and 'skip' not in CATs[key] }

z = {}
all_ips_in_data = []

for domain, values in obj.items():
    reqs, traffic = values['req'], values['traffic']
    ips = values['distinct_ips']

    these_cats = CATs[domain]

    for this_cat in these_cats:
        z.setdefault( this_cat, { 'req': 0, 'traffic': 0, 'distinct_ips': copy.copy([]) } )

        z[this_cat]['req'] += reqs
        z[this_cat]['traffic'] += traffic
        z[this_cat]['distinct_ips'] = list(set( z[this_cat]['distinct_ips'] + ips ))


#pprint(z)

num_ips_in_data = float(len(set( [ x for cat, values in z.items() for x in values['distinct_ips'] ] )))

for cat in z.keys():
    z[cat]['distinct_ips'] = len(set(z[cat]['distinct_ips'])) / num_ips_in_data

z = [ [cat, stats['req'], stats['traffic'], stats['distinct_ips'] ]  for cat, stats in z.items() ]

with open("fig5.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(z)

    print( "Wrote %d categories to fig5.csv" % ( len(z) ) )

