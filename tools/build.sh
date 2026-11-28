#!/bin/sh
# Build the ZIP that people upload to Claude. Run from the repository root.
set -e
# The license travels with the skill: the ZIP and `npx skills add` only take this folder.
cp LICENSE skills/mandarinmaxxing/LICENSE
mkdir -p download
rm -f download/mandarinmaxxing-claude.zip
# The vocabulary table loads the font from the repository, so the installed copy doesn't need it.
(cd skills && zip -qr ../download/mandarinmaxxing-claude.zip mandarinmaxxing -x '*.DS_Store' '*.woff')
echo "download/mandarinmaxxing-claude.zip"
