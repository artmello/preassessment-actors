#!/usr/bin/env bash

set -e

entries=$(df --local -P | rev | cut -f1 -d' ' | rev | tail -n +2 | awk '{ print "\""$0"\""}' | tr '\n' ',' | sed 's/,$//')

echo -e "{\"local_file_systems\": {\"entries\": [${entries}]}}"
