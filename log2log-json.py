#!/usr/local/bin/python3.3
'''
This script takes a .log file (the output from the merge_logs.py) and makes a 

.log.json

which is a dictionary containing the #requests, total traffic, and ips for each .onion domain.

multiple .log.json files will then be merged into a .json file that will then be
combined with categories to make a figure-specific .csv file

'''
import json, codecs, sys, csv, os.path
from pprint import pprint
#from cats import Hs as CATs



#FILENAMES = [ 'logs/2015-11-01.log', 'logs/2015-11-02.log', 'logs/2015-10-01.log', 'logs/2015-10-02.log', 'logs/2015-10-03.log' ]
#FILENAMES = [ 'logs/2015-11-01.log.short' ]

# 1. take in .log files from the command line

reqs, traffics, h2ips = {}, {}, {}
Hs_unlabeled_reqs = {}

FILENAMES = [ x for x in sys.argv[1:] if os.path.isfile(x) and x.endswith('.log') ]
print( "FILENAMES=%s" % FILENAMES )


for fname in FILENAMES:
    print("\n Reading %s..." % fname)
    sys.stdout.flush()

    with codecs.open(fname, encoding='utf-8') as f:

        for line in f:
            try:
                pline = json.loads(line)
            except ValueError:
                sys.stdout.write("x")
                sys.stdout.flush()
            else:
                host = pline['h']
                the_size = int(pline['size']) if 'size' in pline else None
                the_ip = pline['ip'] if 'ip' in pline else None

                if len(host) > 16:
                    host = host[-16:]

                reqs.setdefault(host,0)
                traffics.setdefault(host,0)
                h2ips.setdefault(host,[])

                reqs[host] += 1

                if the_size:
                    traffics[host] += the_size

                if the_ip is not None and the_ip not in h2ips[host]:
                    h2ips[host].append(the_ip)


        # write the output of this .log to a .json
        ofilename = fname + '.json'

        z = { h: {'req': reqs[h], 'traffic': traffics[h], 'ips': sorted(h2ips[h])} for h in reqs.keys() }

        with open(ofilename, 'w') as f:
            json.dump(z, f, indent=True)
            print("Wrote to %s ." % ofilename )



print("\n Done!")

