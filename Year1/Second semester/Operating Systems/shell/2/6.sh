#!/bin/bash

#Write a ashell script that received triplets of command line arguments consisting of a filename, a word and a number (validate input data). For each such triplet, print all the lines in the filename that contain the word exactly k times.

if [ "$#" -eq 0 ]; then
	echo "Enter arguments."
	exit 1
fi

N=$(($# % 3))
if [ ! $N -eq 0 ]; then
	echo "Give 3 arguments at a time."
       exit 1
fi       

N=$(($# / 3))

for trip in $(seq $N)
do
	file=$1
	word=$2
	nr=$3
	while read -r line; do
		touch file.txt
		echo "$line" >> file.txt
		numb=$(grep -E -o "\<$w\>" file.txt | wc -m)
		numb=$((numb / 2))
		if [ $numb -eq $nr ]; then
		       echo "$line"
		fi
		rm file.txt
	done < $file
	shift 3
done
