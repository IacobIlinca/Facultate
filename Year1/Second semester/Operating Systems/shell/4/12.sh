#!/bin/bash

#Scrieti un script bash care primeste un nume de director ca parametru. Cautati recursiv in director si numarati aparitiile fiecarui nume de fisier.

if [ -z "$1" ]; then
	echo "Please provide one argument."
	exit 1
fi

if [ ! -d "$1" ]; then
	echo "The argument should be a directory."
	exit 1
fi

find "$1" -type f | awk -F/ 'print{print $NF}' | sort | uniq -c
