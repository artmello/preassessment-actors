#!/usr/bin/env bash

set -e

cmd="getent group"
entries=$(${cmd} | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"getent_group\": {\"entries\": [${entries}]}}"
