#!/bin/sh

cd merged

# remove any old gzip files
# rm *.gzip

for x in `ls *.log`
do
	echo "sorting  $x..."
	time sort "$x" > "${x%%.*}s.log"

	# remove the old unsorted copy
	rm "$x"

	# the -f is to overwrite any pre-existing filename
	echo "gzipping ${x%%.*}s.log...\n"
	time gzip -f "${x%%.*}s.log"
	mv "${x%%.*}s.log.gz" ../processed/
done
