#!/bin/bash
#Scrieti un script bash care continua sa citeasca siruri de caractere de la tastatura pana cand se introduce numele unui fisier regular.

fanme=""
while [ ! -f "$fname" ]; do
	read -p "Enter a string: " fname
done
