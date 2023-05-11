#!/bin/bash
# request a URL and display the size of the body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
