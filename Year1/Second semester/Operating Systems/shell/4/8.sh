#!/bin/bash

#Scrieti un script bash care sorteaza descrescator dupa dimensiune toate fisierele date ca argumente la linia de comanda. (intai verificati daca un argument e fisier).


while [ "$#" -gt 0 ]; do
	file="$1"
	if [ -f "$file" ]; then
		du -b "$file"
	fi
	shift 1
done | sort -n -r
