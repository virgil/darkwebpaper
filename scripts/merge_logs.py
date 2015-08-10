#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import re, sys
from os import listdir
from os.path import isfile
from pprint import pprint
import os.path

###########################################################################################
INCOMING_DIRECTORY  = '2015-05m/'
#INCOMING_DIRECTORY  = 'incoming/'
MERGED_DIRECTORY = 'merged/'
MINIMUM_NUMBER_OF_LOGFILES = 10
###########################################################################################

PATTERN_SINGLEQUOTE_TO_DOUBLEQUOTE_JSON = re.compile(r"'([^']*)'(?=[:, ])")

def get_parsing_pattern( filename ):
    '''takes the firstline of a file and returns the appropriate regex-pattern for removing the Fastly crud'''

    assert isfile( filename ), "%s was not a file" % filename

    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:

        line = f.readline()

        if not '{' in line and ']:' in line:
            return re.compile(r'^.*]:')

        return re.compile(r'^[^{]*')

def oldstyle2json(line):
    '''takes in the oldstyle log that's double-space delimited and returns json.'''

    month2digit={'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12' }

# { 'time': '2015-07-29 09:40:38', 'cc': 'AT', 'cache': 'HIT', 'host': 'kaufmichob4rdqje', 'status': '200', 'path': '/pictures/alessandra1510/alessandra1510-JnhwGTwpu0v-thumb.jpg' }
    if not '  ' in line:
        return line

    line_values = line.split('  ')


    if len(line_values) != 7:
        print('x'),
        return ''

    line_keys = ['ip','cache','time','h','size','status','path']

    pdict = dict( zip(line_keys, line_values) )


    ### now scrub up the various entries

    # scrub the host
    if pdict['h'].endswith('.onion.city'):
        pdict['h'] = (pdict['h'])[:-len('.onion.city')]

    # scrub the cache
    if pdict['cache'].endswith('-CLUSTER'):
        pdict['cache'] = (pdict['cache'])[:-len('-CLUSTER')]

    # if there's no size, remove it
    if pdict['size'] == '(null)':
        del pdict['size']

    # scrub the HTTP METHOD from the path
    if ' ' in pdict['path'] and pdict['path'].split(' ', 1)[0] in ['GET','HEAD','POST','PUT','TRACE','DELETE']:
        pdict['path'] = pdict['path'].split(' ', 1)[1]

    # scrub the timestamp
    timelist = pdict['time'].split(' ')
    timedict = { 'day': timelist[1], 'month': month2digit[timelist[2]], 'year': timelist[3], 'time': timelist[4] }
    pdict['time']="%(year)s-%(month)s-%(day)s %(time)s" % timedict


    z = [ '"%s": "%s"' % (x, pdict[x]) for x in ['time', 'cache', 'h', 'status', 'size', 'path', 'ip'] if x in pdict ]
    z = '{ ' + ', '.join(z) + ' }'

    return z

###########################################################################################
#from os.path import isfile, join
#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
def process_log_files( input_filenames, output_filename ):
    '''returns the output filename'''

# old style.  Remove everything before the ']:', else, before the first '{'

    output = open( output_filename, 'w', encoding='utf-8' )

    for filename in input_filenames:

        # is this really a file?
        if not isfile( filename ):
            print("File: '%s' does not exist. Skipping." % filename, file=sys.stderr)
            continue

        pattern = get_parsing_pattern( filename )

        with open(filename,'r', encoding='utf-8', errors='ignore') as f:

            for line in f:

                # remove everything before the first '::'.  Then remove any whitespace.
                newline = re.sub(pattern, '', line, count=1).strip()

                # if this is a JSON file with the single-quote problem, fix that now.
                if "'time':" in newline:
                    newline = re.sub(PATTERN_SINGLEQUOTE_TO_DOUBLEQUOTE_JSON, r'"\1"', newline).strip()

                # if this isn't a JSON line, convert it from the double-space version to JSON.
                if not newline.startswith('{'):
                    newline = oldstyle2json(newline).strip()

                # if this file has the "host": key in it, rewrite it to "h":
                if '"host":' in newline:
                    newline = newline.replace('"host":','"h":', 1)

                output.write( newline )
                output.write('\n')


    # finished with all of the files
    output.close()

    return os.path.abspath( output_filename )

def fname2day(fname):
    '''returns the day of a log filename'''

    path, name = os.path.split(fname)

    if 'T' in name:
        return name.split('T',1)[0]

    return None

def make_dict_of_dates_to_logs():
    '''returns a dictionary of all of the dates to process with their logfiles'''
    # get all of the *.log files...
    all_files = [ os.path.abspath(INCOMING_DIRECTORY + x) for x in listdir(INCOMING_DIRECTORY) if x.upper().endswith('.LOG') ]
    all_days = sorted(list(set([ fname2day(x) for x in all_files ])))

    # remove the final day because we're not sure if it's done yet
    #all_days.pop()

    print( "days to process: %s" % ' '.join(all_days) )

    # make a dictionary of all of the logfiles for each day
    z = { x:[] for x in all_days }

    for this_file in all_files:
        this_day = fname2day(this_file)
        z[this_day].append( this_file )

    return z 


if __name__ == '__main__':

    dicty = make_dict_of_dates_to_logs()

    # remove any entries without enough entries from the dicty
    for date in sorted(dicty.keys()):

        input_logfiles = dicty[date]

        # if there's too log files, skip it.
        if len(input_logfiles) < MINIMUM_NUMBER_OF_LOGFILES:
            print("* Warning: Only %d logfiles for %s.  Skipping." % (len(input_logfiles), date) )
            del dicty[date]
            

    for date in sorted(dicty):

        input_logfiles = dicty[date]

        ofilename = "%s/%s.log" % ( MERGED_DIRECTORY, date ) 
        abs_ofilename = os.path.abspath(ofilename)

        #print( "Doing %s..." % date)
        #print( "ofile=%s" % abs_ofilename )
        #print( "inputs=%s" % logfiles )

        print( "- Merging %d file(s) \t -> %s" % (len(input_logfiles), abs_ofilename) )
        process_log_files( input_logfiles, abs_ofilename )
        


