#!/bin/bash
# make the server say "you got me"
curl -s -X PUT -d "user_id=98" -L 0.0.0.0:5000/catch_me
