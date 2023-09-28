#!/bin/bash
# Prints the size of the body of the response
curl -I -s $1 | grep Content-Length | cut -d " " -f2
