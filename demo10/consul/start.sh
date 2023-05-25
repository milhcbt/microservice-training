#!/bin/sh
consul agent -dev -client 0.0.0.0 &
# Wait for consul service to start before importing configuration
sleep 10
consul kv import @/config.json
# Keep script running so container doesn't exit
tail -f /dev/null
