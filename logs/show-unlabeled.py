#!/usr/bin/python
'''
In this script we print the unlabeled popular entries of a single .json file
'''

import json, codecs, sys, os.path, copy
from pprint import pprint
from cats import Hs as CATs




# 1. take in .log.json files from the command line

fnames = [ x for x in sys.argv[1:] if os.path.isfile(x) and x.endswith('.json') ]

assert len(fnames) == 1, "Can only specify ONE .json file!" 
fname = fnames[0]

obj = None
with codecs.open(fname, encoding='utf-8') as f:
    obj = json.load(f)

# get all domains in obj that arent categorized
uncategorized = [ domain for domain in obj.keys() if domain not in CATs and len(domain) == 16 ]

# not get the req for each of the unlabeled
# for each domain, get the #reqs
reqs = sorted([ (obj[domain]['req'], str(domain)) for domain in uncategorized ], reverse=True)

# print the top 20
pprint(reqs[:20])

