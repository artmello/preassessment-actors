#!/usr/bin/env bash

input=""
while read line
do
  input+=${line}
done < /dev/stdin

inport="rpm_qa"
key="entries"

entries=$(echo ${input} | python -c "\
import json, sys
obj=json.load(sys.stdin)
ret=[]
for i in obj[\"${inport}\"][\"${key}\"]:
  e=', '.join([\"\\\"{}\\\":\\\"{}\\\"\".format(str(k), str(v)) for k, v in i.items()])
  ret.append(\"{\" + e + \"}\")
print('|'.join(ret))")

IFS="|"
signed_pkgs=""
for e in ${entries}; do
  if [[ ${e} == *"199e2f91fd431d51"* ]] || \
     [[ ${e} == *"5326810137017186"* ]] || \
     [[ ${e} == *"938a80caf21541eb"* ]] || \
     [[ ${e} == *"fd372689897da07a"* ]] || \
     [[ ${e} == *"45689c882fa658e0"* ]]; then
    signed_pkgs+="${e}#"
  fi
done  

entries=$(echo ${signed_pkgs} | tr '#' '\n'| tr '\n' ',' | sed 's/[,]*$//')
echo -e "{\"redhat_signed_pkgs\": {\"entries\": [${entries}]}}"
