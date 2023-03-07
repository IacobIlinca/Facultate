#!/bin/bash

#Scrieti un script bash care afiseaza toate fisierele text dintr-un director specificare(daca nu se specifica niciun director, se va folosi directorul curent). Pentru toate fisierele gasite, scriptul  va raporta dimensiunea fiecaruia, permisiunile si numarul de linii unice.

dir=${1:-"."}

if [ -d "$dir" ]; then
	for f in $(find "$dir" -type f); do
		if file $f | grep -E -q "text"; then
			size=$(du -b $f | cut -f1)
			perm=$(ls -l $f | cut -d' ' -f1)
			lines=$(sort $f | uniw | wc -l)
			echo "Filename: $f -size: $size -permission: $perm -unique lines: $lines"
		fi
	done
fi

