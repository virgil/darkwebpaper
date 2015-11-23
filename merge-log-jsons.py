#!/usr/local/bin/python3.3
'''
In this script we take a bunch of .log.json's and merge them into a single .log.json
'''

import json, codecs, sys, os.path, copy
from pprint import pprint
#from cats import Hs as CATs



# 1. take in .log.json files from the command line
FILENAMES = [ x for x in sys.argv[1:] if os.path.isfile(x) and x.endswith('.json') ]
print( "FILENAMES=%s" % FILENAMES )

y = {}
for fname in FILENAMES:
    print("\n Reading %s..." % fname)
    sys.stdout.flush()

    with codecs.open(fname, encoding='utf-8') as f:
        obj = json.load(f)

        for domain, values in obj.items():
            req = int(values['req']) if 'req' in values else 0
            traffic = int(values['traffic']) if 'traffic' in values else 0
            ips = values['ips'] if 'ips' in values else []

            if domain not in y:
                y[domain] = { 'req': req, 'traffic': traffic, 'ips': ips }
                continue

            y[domain]['req'] += req
            y[domain]['traffic'] += traffic
            y[domain]['ips'] = list(set( y[domain]['ips'] + ips ))


# set the ips to the COUNT of uniq IPs
z = {}
for domain, values in y.items():
    req, traffic, ips = int(values['req']), int(values['traffic']), values['ips']
    z[domain] = { 'req': req, 'traffic': traffic, 'distinct_ips': list(set(ips)) }



with open("out.log.json", "w") as f:
    json.dump(z, f, indent=True)
    print( "Wrote %d domains to out.log.json" % ( len(z) ) )

print("\n Done!")

