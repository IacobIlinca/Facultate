#!/bin/bash

#Write a script that reads filenames and check for each file how many words contsians on the first line and the size of the file. Perform all required validations on the inpit data.

if [ "$#" -lt 1 ]; then
	echo "Not enough arguments."
	exit 1
fi

for F in "$@"; do
	if [ ! -f "$F" ]; then
		echo "$F is not a file!"
	else 
		nr=$(grep -m 1 "." $F | wc -w)
		size=$(du -b $F | awk -F" " '{print $1}')
		echo "For file: $F , size- $size, nr- $nr"
	fi
done
