#!/bin/bash

#Scrieti un script shell care primeste ca argumente nume de procese. Scriptul va monitoriza toate procesele din sistem si, cand apare un proces cu unul din numele specificat, scriptul il va intrerupe si va afisa un mesaj. (Folositi comenzile ps, kill, killal). 

if [ "$#" -eq 0 ]; then
	 echo "Provide at least one name."
	 exit 1
fi

while true; do
	for proces in "$@"; do
		pids=""
		pids=$(ps -ef | awk '{print $8" $2}' | grep -E "\<$proces " | awk '{print $2}')
		if [ -n "$pids" ]; then
			kill -9 "$pids"
		fi
	done
done



