#!/bin/sh

# Script to serve event stream
echo "Content-Type: text/event-stream"
echo ""

# Generate events
while true; do
    if ! [ -f messages ] ; then
        touch messages
    fi
    tail -f messages
done
