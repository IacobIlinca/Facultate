#!/bin/bash

#Scrieti un script bash care afiseaza o data pe secunda numarul de procese per user sortat descresctor dupa numarul de procese, pentru toti utilizatorii dati ca argumente la linia de comanda. Daca niciun utilizator nu e specificat la linia de comanda, scriptul va afisa informatiile pentru toti utilizatorii din sistem.

users="-e"
if [ "$#" -gt 0 ]; then
	users=""
	for user in "$@"; do
		users="$users -u $user"
	done
fi

while tru; do
	clear
	ps -f $users | awk 'NR > 1{print $1}' | sort | uniq -c | sort -n -r -k1,1
	sleep 1
done
