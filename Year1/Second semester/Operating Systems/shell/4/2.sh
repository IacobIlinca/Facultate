#!/bin/bash

#Scrieti un script bash care primeste oricate argumente la linia de comanda si afiseaza pe ecran, pentru fiecare argument, daca este un fisier, un director, un numar sau altceva."

if [ "$#" -eq 0 ]; then
	echo "No argument was given!"
	exit 1
fi

while [ ! "$#" -eq 0 ]; do
       arg=$1
	if [ -d "$arg" ]; then
	 echo "$arg is a directory"
 	elif [ -f "$arg" ]; then
         echo "$arg is a file"
	elif echo "$arg" | grep -E -q "^[0-9]+$"; then
          echo "$arg is a number"
	else
          echo "$arg is something else"
	fi
	shift
done

