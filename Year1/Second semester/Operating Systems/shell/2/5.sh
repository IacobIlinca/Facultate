#!/bin/bash
#Write a shell script that for each command line parameter will do:
#-if it's a file, print the name, number of characters and lines in the file
#-if it's a directory, print the name and how many files it contains (including subdirectories files)

if [ "$#" -eq 0 ]; then
	echo "Give arguments!"
	exit 1
fi

for A in "$@"; do
	if [ -f "$A" ]; then
		nrc=$(grep -E '.' $A | wc -m)
		nrl=$(grep -E '.' $A | wc -l)
		echo "$A: nrc- $nrc ,nrl- $nrl"
	elif [ -d "$A" ]; then
		nr=$(find dir | awk -F"/" '{print $NF}' | wc -l)
		echo "$A: $nr"
	fi
done
