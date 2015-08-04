#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
import re, sys
from os import listdir
from os.path import isfile
from pprint import pprint
import os.path

###########################################################################################
INCOMING_DIRECTORY  = 'incoming/'
PROCESSED_DIRECTORY = 'processed/'
TEMP_DIRECTORY = 'tmp/'
###########################################################################################

###########################################################################################
#from os.path import isfile, join
#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
def process_log_files( input_filenames, output_filename ):
    '''returns the output filename'''

    # remove everything before the first '{'
    pattern = re.compile(r'^[^{]*')

    output = open( output_filename, 'w', encoding='utf-8' )

    for filename in input_filenames:

        # is this really a file?
        if not isfile( filename ):
            print("File: '%s' does not exist. Skipping." % filename, file=sys.stderr)
            continue

        with open(filename,'r', encoding='utf-8', errors='ignore') as f:
            for line in f:

                # remove everything before the first '::'.  Then remove any whitespace.
                newline = re.sub(pattern, '', line, count=1).strip()

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
    all_days.pop()

    print( "days to process: %s" % all_days )

    # make a dictionary of all of the logfiles for each day
    z = { x:[] for x in all_days }

    for this_file in all_files:
        this_day = fname2day(this_file)

        if this_day in all_days:
            z[this_day].append( this_file )

    return z 


if __name__ == '__main__':

    dicty = make_dict_of_dates_to_logs()

    for date in sorted(dicty):
        input_logfiles = dicty[date]
        ofilename = "%s/%s.log" % ( TEMP_DIRECTORY, date ) 
        abs_ofilename = os.path.abspath(ofilename)

        #print( "Doing %s..." % date)
        #print( "ofile=%s" % abs_ofilename )
        #print( "inputs=%s" % logfiles )

        process_log_files( input_logfiles, abs_ofilename )
        print( "- Merged %d file(s) \t -> %s" % (len(input_logfiles), abs_ofilename) )


