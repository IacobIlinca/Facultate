#!/bin/bash

#Scrieti un script bash care primeste ca argumente la linia de comanda perechi de nume de fisier si cuvant. Pentru fiecare pereche, afisati un mesaj daca in fisier cuvantul dat apare de cel putin 3 ori.

if [ "$#" -lt 2 ]; then
	echo "Please provide at least 2 arguments."
	exit 1
fi

if [ $(($# % 2)) -eq 1 ]; then
	echo "You must give an even number of arguments."
	exit 1
fi

while [ $# -gt 1 ]; do
	file="$1"d
	word="$2"

	if [ ! -f "$file" ]; then
		echo "Name $file is not a file!"
	else
		count=$(grep -E -o "\<$word\>" "$file" | wc -l)
		if [ $count -ge 3 ]; then
			echo "Word $word appears $count times in file $file"
		fi
	fi
	shift 2
done

if [ "$#" -eq 1 ]; then
	echo "Pair incomplete!"
fi
