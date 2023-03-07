#!/bin/bash

#Scrieti un script bash care numara toate liniile de cod din fisierele C continute de un director dat ca argument la linia de comanda, excluzand liniile goale sau cele care contin doar spatii.

if [ "$#" -lt 1 ]; then
	echo "Not enough arguments were given!"
	exit 1
fi

if [ ! -d "$1" ]; then
	echo "It is not a folder!"
	exit 1
fi

total=0

for f in $(ls "$1" | grep -E "\.c$" ); do
	if [ -f "$1/$f" ]; then
		nr_lines=$(grep -E -c -v "^[ \t]*$" "$1/$f" )
		echo ""$f":"$nr_lines""
		total=$((total+nr_lines))
	fi
done
echo "Total line: $total"

