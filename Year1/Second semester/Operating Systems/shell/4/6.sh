#!/bin/bash

#Scrieti un script bash care citeste nume de fisiere pana cand se introduce cuvantul "stop".
#Pentru fiecare nume de fisier, verificati daca este un fisier text, daca da, afisati numarul de cuvinte de pe prima linie. (Folositi test ca sa verificati daca un string este un nume de fisier si comanda file ca sa verificati daca fisierul este text).

while true; do
	read -p "Enter a file name or stop to stop: " file
	if [ "$file" = "stop" ]; then
		echo "Done."
		exit 0
	elif [ -f "$file" ]; then
		if file $file | grep -E -q "text"; then
			echo "File: $file -Words on first line: $(head -1 $file | wc -w )"
		fi
	fi
done

