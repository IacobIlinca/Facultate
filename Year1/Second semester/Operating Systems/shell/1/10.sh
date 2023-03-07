#!/bin/bash
result=""
for user in $( last | awk '{print $1}' | sort | uniq)
do
	count=$( last | grep -Ec "^{user}")
	result="$result$count $user"$'\n'
done

result=$(echo "$result" | sort -n -r -k 1,1)
echo "$result"

