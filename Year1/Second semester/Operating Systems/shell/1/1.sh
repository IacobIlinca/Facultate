#!/bin/bash
for user in $(who | awk '{print $1}')
do
	proc=$(ps -ef | grep -Ec "^${user}")
	echo " $user $proc"
done

