#!/bin/bash

#Same as 1, but input by command line arguments.

while true
do
	read file_name
	if [ "$file_name" == "stop" ]; then
		exit 0
	elif [ ! -f "$file_name" ]; then
		echo "$filename is not a file!"
	else
		nr=$(grep -m 1 "." $file_name | wc -w)
		size=$(du -b $filename | awk -F" " '{print $1}')
		echo "$file_name: size - $size, nr- $nr"
	fi
done
