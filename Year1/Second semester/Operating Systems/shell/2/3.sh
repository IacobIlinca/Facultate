#!/bin/bash

#Write a shell script that receives as argument a natural number N and generate N text files:
#-the name of the filesc will be of the form:vfile_X, where X={1,2,...,N}
#-each generated file will contain online lines between X and X+5 of the file /etc/passwd 


if [ "$#" -eq 0 ]; then
	echo "Enter a number N!"
	exit 1
fi

N=$1
C=300
d=305
for A in $(seq $N)
do
	touch file_$A
	sed -n ''$C', '$D'p' /etc/passwd >> file_$A
	C=$(($C + 5))
	D=$(($D + 5))
done
