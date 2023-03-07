#!/bin/bash

#Scrieti un script bash care sorteaza fisierele date ca argumente la linia de comanda in ordinea crescatoare a dimensiunii lor in octeti.

for f in "$@"; do
	if [ -f "$f" ]; then
		du -b "$f"
	fi
done | sort -n
