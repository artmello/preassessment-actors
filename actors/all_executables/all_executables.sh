#!/usr/bin/env bash

input=""
while read line
do
  input+=${line}
done < /dev/stdin

inport="local_file_systems"
key="entries"

local_file_systems=$(echo ${input} | python -c "\
import json, sys
obj=json.load(sys.stdin)
print(' '.join([str(i) for i in obj[\"${inport}\"][\"${key}\"]]))")

executables=""
for fs in ${local_file_systems}; do
  executables+=$(find ${fs} -xdev -perm /111 -print)
done  

entries=$(echo ${executables} | tr ' ' '\n' | sort | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"all_executables\": {\"entries\": [${entries}]}}"
