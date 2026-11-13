#!/bin/sh
# Build the ZIP that people upload to Claude. Run from the repository root.
set -e
mkdir -p dist
rm -f dist/mandarinmaxxing-claude.zip
(cd skills && zip -qr ../dist/mandarinmaxxing-claude.zip mandarinmaxxing -x '*.DS_Store')
echo "dist/mandarinmaxxing-claude.zip"
