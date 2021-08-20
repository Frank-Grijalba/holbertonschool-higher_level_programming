#!/bin/bash
# a Bash script that get the method and show the response
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
