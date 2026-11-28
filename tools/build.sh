#!/bin/sh
# Build the ZIP that people upload to Claude. Run from the repository root.
#   sh tools/build.sh         the release ZIP: the lesson templates load the scripts from the version's tag
#   sh tools/build.sh test    a ZIP to try before a release: they load them from the current commit, which must be pushed
set -e
VERSION="v$(python3 -c "import json; print(json.load(open('plugin.json'))['version'])")"
# The templates name the version whose scripts they load. Stop if one is out of step with plugin.json.
for f in skills/mandarinmaxxing/setup.md skills/mandarinmaxxing/lesson-format.md; do
  if grep -o 'mandarinmaxxing@[^/]*/' "$f" | grep -qv "mandarinmaxxing@$VERSION/"; then
    echo "$f loads scripts from another version than $VERSION: update its script lines." >&2
    exit 1
  fi
done
# The license travels with the skill: the ZIP and `npx skills add` only take this folder.
cp LICENSE skills/mandarinmaxxing/LICENSE
mkdir -p download
OUT=download/mandarinmaxxing-claude.zip
STAGE=$(mktemp -d)
cp -R skills/mandarinmaxxing "$STAGE/mandarinmaxxing"
if [ "$1" = "test" ]; then
  OUT=download/mandarinmaxxing-claude-test.zip
  COMMIT=$(git rev-parse HEAD)
  sed -i.bak "s#mandarinmaxxing@$VERSION/#mandarinmaxxing@$COMMIT/#g" "$STAGE/mandarinmaxxing/setup.md" "$STAGE/mandarinmaxxing/lesson-format.md"
  rm -f "$STAGE"/mandarinmaxxing/*.bak
fi
rm -f "$OUT"
# The vocabulary table loads the font from the repository, so the installed copy doesn't need it.
(cd "$STAGE" && zip -qr - mandarinmaxxing -x '*.DS_Store' '*.woff' '*__pycache__*') > "$OUT"
rm -rf "$STAGE"
echo "$OUT"
