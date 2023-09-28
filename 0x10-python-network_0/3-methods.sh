#!/bin/bash
# get allowed methods
curl -Is $1 | grep "Allow: " | cut -c 8-
