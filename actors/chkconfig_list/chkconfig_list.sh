#!/usr/bin/env bash

set -e


cmd="chkconfig --list"
entries=$(${cmd} 2> /dev/null | awk '{$1=$1}{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"chkconfig_list\": {\"entries\": [${entries}]}}"
