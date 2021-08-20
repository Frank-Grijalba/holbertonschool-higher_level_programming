#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
# not allowed to use any pipe, redirection, not allowed to use ; and &&
curl -sI "$1" -w '%{http_code}' -o /dev/null
