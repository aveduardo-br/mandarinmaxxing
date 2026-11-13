#!/bin/sh
# Build the ZIP that people upload to Claude. Run from the repository root.
set -e
mkdir -p download
rm -f download/mandarinmaxxing-claude.zip
(cd skills && zip -qr ../download/mandarinmaxxing-claude.zip mandarinmaxxing -x '*.DS_Store')
echo "download/mandarinmaxxing-claude.zip"
