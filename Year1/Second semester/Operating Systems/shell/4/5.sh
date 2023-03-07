#!/bin/bash

#Scrieti un script bash care calculeaza suma in octeti a tuturor fisierelor regulare dintr-un director dat ca argument. (folositi test ca sa verificati daca directorul dat exits asi daca un fisier este fisier regular.)

if [ ! "$#" -eq 1 ]; then
	echo "Give exactly one directory as argument!"
	exit 1
fi

if [ ! -d "$1" ]; then
	echo "The argument shoul be a directory"
	exit 1
fi

sum=0
for f in $(ls $1); do
	if [ -f "$1/$f" ]; then
		size=$(du -b "$1/$f" | awk '{print $1}')
		echo "File: $f with size: $size. "
		sum=$((sum+size))
	fi
done
echo "Total size of regular files from directory $1 is: $sum. "
