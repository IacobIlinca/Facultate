#!/bin/bash

#Fie un fisier care contine mai multe nume de utilizator, fiecare pe linie separata. Generati un string de email-uri separate de virgula. Adresele de email se vor obtine concatenand "@scs.ubbcluj.ro" la numele de utilizator. Stringul generat trebuie sa nu se termine cu caracterul virgula.

if [ -z "$1" ]; then
	echo "Please enter an input file!"
	exit 1
fi

if [ ! -f "$1" ]; then
	echo "The given argument is not a file!"
	exit 1
fi

result=""
for u in $(cat "$1"); do
	result="$u@scs.ubbcluj.ro,$result"
done

result=$(echo $result | sed -E "s/,$//")
echo $result
