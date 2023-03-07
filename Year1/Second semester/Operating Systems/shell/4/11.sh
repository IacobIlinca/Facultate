#!/bin/bash

#Gasiti recursiv intr-un director dat toate legaturile simbolice si raportati care din ele sunt legate de fisiere/directoare care nu exista. Folositi optiunea -L de la test pentru a verifica daca un string este un linl simbolic si optiunea -e ca sa verificati daca este valid (test va returna false daca fisierul/directorul referit de legatura simbolica nu exista).

for link in $(find "$1" -type l); do
	if [ ! -e "$link" ]; then
		echo "Link $link is not valid!"
	fi
done
