#!/bin/bash
#Scrieti un script bash care numara toate liniile de cod din fisierele C continute de un director dat ca argument la linia de comanda si toate subdirectoarele acestuia, excluzand liniile goale sau cele care contin doar spatii.

if [ "$#" -lt 1 ]; then
	echo "Not enough arguments were given!"
	exit 1
fi

if [ ! -d "$1" ]; then
	echo "A folder should be given!"
	exit 1
fi

for f in $(find "$1" -type f | grep -E "\.c$"); do
	nr_lines=$(grep -E -c -v "^[ \t]*$" $f )
	echo "$f:$nr_lines"
	total=$((total+nr_lines))
done
echo "Total:$total"
