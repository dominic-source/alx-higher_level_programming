#!/bin/bash
# make the server say "you got me"
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "origin: School"
