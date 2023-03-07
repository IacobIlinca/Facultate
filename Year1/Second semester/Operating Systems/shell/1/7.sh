#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "ERROR:Provide exactly one file as argument."
	exit 1
fi

final=""
for line in $(cat $1)
do
	current=$(echo $line | sed -E 's/^(.+)$/\1@scs.ubbcluj.ro/')
	final="$final,$curent"
done
echo ${final:1}
