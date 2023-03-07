#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "ERROR:should give exactly one director as argv."
	exit 1
fi

count=0
for file in $(find $1 -name '*.log')
do
	sort $file -o $file
	((count++))
done

excho "Sorted $count log files."
