#!/usr/local/bin/python3.3

import json, codecs, sys, csv
from pprint import pprint

import pycountry

#FILENAMES = ['logs/2015-04-01.log','logs/2015-05-01.log','logs/2015-06-01.log','logs/2015-07-01.log','logs/2015-08-01.log','2015-09-01.log','logs/2015-10-01.log','logs/2015-10-02.log', 'logs/2015-10-03.log', 'logs/2015-10-05.log', 'logs/2015-10-06.log']
FILENAMES = ['logs/2015-09-01.log.short']

#help

reqs = {}
traffics = {}

for fname in FILENAMES:
    print("\n Reading %s..." % fname)
    sys.stdout.flush()
    
    with codecs.open(fname, encoding='utf-8') as f:
        
        for line in f:
            try:
                pline = json.loads(line)
                
                if 'cc' not in pline:
                    continue

            except ValueError:
                sys.stdout.write("X")
            else:
                cc, cn = pline['cc'], 'Unknown'
                try:
                	country = pycountry.countries.get(alpha2=cc)
                	cn = country.name
                except:
                	if cc == 'EU':
                		cn = 'Europe'
                	elif cc == 'A1':
                		cn = 'Anonymous Proxy'
                	elif cc == 'AP':
                		cn = 'Asia Pacific'
                	else:
                		cn = 'Other'

                reqs.setdefault(cn,0)
                traffics.setdefault(cn,0)

                reqs[cn] += 1
                if 'size' in pline:
                    traffics[cn] += int(pline['size'])

print("\n Done!")


z = [ [cn,reqs[cn],traffics[cn]] for cn in reqs.keys() ]
    
with open("fig2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(z)

