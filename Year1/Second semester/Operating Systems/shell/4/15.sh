#!/bin/bash

#Scrieti un script care primeste un director ca parametru la linia de comanda. Scriptul va sterge toate fisierele sursa C din director si va afisa celelalte fisiere sortate alfabetic.

if [ ! "$#" -eq 1 ]; then
	echo "Give exactly one name as argument!"
	exit 1
fi

if [ ! -d "$1" ]; then
	echo "The argument should be a directory."
	exit 1
fi

for file in $(find $1 -type f ); do
	if [ echo "$file" | grep -E -c "\.c$" ]; then
		rm "$file"
	fi
done | sort 
