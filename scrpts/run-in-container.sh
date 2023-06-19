#!/bin/bash

docker run \
    --network webscarping -p 9999:9999 -v $(pwd):/app \
    -w /app --platform linux/amd64 --rm -it python:3.9.4 /bin/bash
