#!/bin/sh

echo "Arguments: $*"

trap 'echo "SIGTERM received"; exit 0' TERM

while true; do
    echo "Application is running..."
    sleep 1 &
    wait $!
done