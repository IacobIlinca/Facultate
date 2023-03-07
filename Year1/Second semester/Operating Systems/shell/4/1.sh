#!/bin/bash
#Scrieti un script bash care numara toate fisierele C dintr-un director dat si toate subdirectoarele sale.

if [ "$#" -lt 1 ]; then
	echo "Not enough arguments!"
	exit 1
fi

fin $1 -type f | grep -E -c "\.c$"
