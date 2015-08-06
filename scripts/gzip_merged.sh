#!/bin/sh


if [ ! -d "$1" ]; then
	echo "You must specify a directory."
	echo "E.g. ./gzip_merged.sh merged/"
	exit
	fi

# strip any slash from dir
dir=${1%/}

for x in ${dir}/*.log
do
	# the -f is to overwrite any pre-existing filename
	echo "gzipping ${x}..."
	time gzip -f "$x"
done
