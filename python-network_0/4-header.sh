#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request with specific header using curl
curl -sH "X-HolbertonSchool-User-Id: 98" "$1" -X GET
