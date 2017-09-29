#!/usr/bin/env bash

input=""
while read line
do
  input+=${line}
done < /dev/stdin

inport="rpm_va"
key="entries"

entries=$(echo ${input} | python -c "\
import json, sys
obj=json.load(sys.stdin)
print('|'.join([str(i) for i in obj[\"${inport}\"][\"${key}\"]]))")

IFS='|'
changed_config=""
for e in ${entries}; do
  if [[ ${e} == *"c /"* ]]; then
    changed_config+="|${e}"
  fi
done  

IFS=' '
entries=$(echo ${changed_config} | tr '|' '\n' | sort | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"changed_config\": {\"entries\": [${entries}]}}"
