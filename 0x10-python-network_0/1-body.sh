#!/bin/bash
# Prints the content of the body of the response if it is status 200
curl -IsX GET $1 | grep -qE "HTTP/1.+ 200" && curl -sX GET $1
