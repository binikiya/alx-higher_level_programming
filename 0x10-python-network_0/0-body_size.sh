#!/usr/bin/bash
# Takes in a URL, sends a request to the URL, and displays size of body
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
