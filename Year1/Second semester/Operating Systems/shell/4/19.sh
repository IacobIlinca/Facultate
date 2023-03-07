#!/bin/bash

#Scrieti un script shell care,pentru toti utilizatorii din /etc/passwd, creeaza un fisier cu acelasi nume ca al utilizatorului in care se salveaza toate adresele ip de pe care s-a logat acel utilizator. (folositi comanda last ca sa obtineti adresele ip la care s-a logat un user)


destination="./results"

if [ ! -d $destination ]; then
	if [ ! -e $destination ]; then
		mkdir $destinatiom
	else
		echo "The file $destination already exists and it is not a dictionary. Exiting!"
		exit 1
	fi
fi

users=$(awk -F: '{print $1}' /etc/passwd)

for user in "$users"; do
	ips=$(last $user | head -n -2 | awk '{print $3}' | sort | uniq)
	if [ -n "$ips" ]; then
		echo "$ips" > $destination/$user
	fi
done

