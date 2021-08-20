#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" -X POST | grep Allow |cut -d':' -f2 | sed 's/^[[:space:]]*//'
