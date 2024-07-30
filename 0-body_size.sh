#!/usr/bin/python3
# display Content-Length
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
