#!/usr/bin/env bash

set -e

cmd="rpm -qal"
entries=$(${cmd} | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"rpm_qal\": {\"entries\": [${entries}]}}"
