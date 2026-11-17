#!/bin/bash
# waitfor.sh FILE : blocks until FILE exists (up to ~9 minutes). Prints ok or timeout.
for i in $(seq 1 270); do [ -e "$1" ] && { sleep 1; echo ok; exit 0; }; sleep 2; done; echo timeout
