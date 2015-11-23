#!/usr/local/bin/python3.3
'''
This script prints the 10 most popular domains by requests in the data-set
'''

import json, codecs, sys, csv, copy
from pprint import pprint

from cats import Hs as CATs

def get_rank( the_domain, the_key, the_obj ):
    '''returns the rank at which 'the_domain' appears in the_list'''
    # get the value of the_domain's the_key in the_obj.

    domain_value = the_obj[the_domain][the_key]
    #print( "domain_value=%s" % domain_value )

    sorted_uniq_values = sorted(list(set([ x[the_key] for x in the_obj.values() ])),reverse=True)

    # return the index of the domain_value in the sorted_uniq_values
    z = sorted_uniq_values.index(domain_value) + 1

    return z




fname = 'logs/aggregate-oct-nov.json'

obj = None
with codecs.open(fname, encoding='utf-8') as f:
    obj = json.load(f)


# set all of the distinct_ips to the num of distinct IPs
for d in obj.keys():
    obj[d]['distinct_ips'] = float(len(set(obj[d]['distinct_ips'])))

ds_to_delete = [ d for d in obj.keys() if len(d) != 16 ]

for d in ds_to_delete:
    del obj[d]

#Get all of the domains in obj that have a category
#obj = { key:value for key,value in obj.items() if key in CATs and 'skip' not in CATs[key] }

#z = {}


NUM_TOP_ITEMS = 15
to_use = sorted([ (values['distinct_ips'],d) for d,values in obj.items() if len(d) == 16], reverse=True)

z_domains = ([ domain for req, domain in to_use ])[:NUM_TOP_ITEMS]

# now get the ranks for the each category
ranks_reqs = [ get_rank(d, 'req', obj) for d in z_domains ]
ranks_traffic = [ get_rank(d, 'traffic', obj) for d in z_domains ]
ranks_ips = [ get_rank(d, 'distinct_ips', obj) for d in z_domains ]

cats = [ str( ', '.join(list(CATs[d])) ) for d in z_domains ]

print(r'''
\begin{table}
\begin{tabular}{ l | r r r l }
\hline
\textbf{Domain} & \textbf{Users} & \textbf{Requests} & \textbf{Traffic} & \textbf{Labels} \\
\hline
''')


for d, ip, req, traffic, cat in zip(z_domains, ranks_ips, ranks_reqs, ranks_traffic, cats):

    # clean up the output
    cat = cat.replace('&',r'\&')
    if 'childabuse' in cat:
        print("%% %s" % d )
        d = d[:8] + (r'\textunderscore' * 8)

    print("\\texttt{%s} & %s & %s & %s & %s \\\\" % (d,ip,req,traffic,cat) )


print(r''' 
\hline
\end{tabular}

\caption{Ranks for the ten popular .onion domains.}
\end{table}
''')








