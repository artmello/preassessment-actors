#!/usr/bin/env bash

set -e


IFS=$'\n' 
entries=$(rpm -Va | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"rpm_va\": {\"entries\": [${entries}]}}"
