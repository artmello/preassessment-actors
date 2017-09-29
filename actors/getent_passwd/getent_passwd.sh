#!/usr/bin/env bash

set -e

cmd="getent passwd"
entries=$(${cmd} | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"getent_passwd\": {\"entries\": [${entries}]}}"
