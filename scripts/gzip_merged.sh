#!/bin/sh

cd merged

# remove any old gzip files
# rm *.gzip

for x in `ls *.log`
do
#	echo "sorting  $x..."
#	time sort "$x" > "${x%%.*}s.log"

#	# remove the old unsorted copy
#	rm "$x"

	# the -f is to overwrite any pre-existing filename
	echo "gzipping ${x}...\n"
	time gzip -f "$x"
	mv "${x}.gz" ../processed/
done
