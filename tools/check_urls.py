"""Visit every address the lesson's HTML depends on, before a release.

Usage: python3 tools/check_urls.py [REF]

The table and the setup card load their scripts from this repository through jsDelivr,
by the version's tag. A tag doesn't exist until its release is published, so pass the
commit to test (REF, as in the release workflow): the addresses are tried at that commit.
It checks the two scripts, the font, the stroke-order library, and a sample of the word
recordings named in web/vocab.js. Exit code 1 if any address fails.
"""
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKILL = os.path.join(ROOT, 'skills', 'mandarinmaxxing')
SAMPLE = ['你好', '谢谢', '还', '还_hua2n', '银行', '尽管']


def main(ref=None):
    urls = []
    for name in ('setup.md', 'lesson-format.md'):
        urls += re.findall(r'<script src="([^"]+)"', open(os.path.join(SKILL, name), encoding='utf-8').read())
    vocab = open(os.path.join(SKILL, 'web', 'vocab.js'), encoding='utf-8').read()
    urls += re.findall(r"lib\.src = '([^']+)'", vocab)
    audio = re.search(r"var AUDIO = '([^']+)'", vocab).group(1)
    urls += [audio + urllib.parse.quote(word) + '.mp3' for word in SAMPLE]
    table = next(u for u in urls if u.endswith('web/vocab.js'))
    urls.append(table.replace('web/vocab.js', 'fonts/kaiti-hsk-1-6.woff'))
    if ref:
        urls = [re.sub(r'(aveduardo-br/mandarinmaxxing)@[^/]+/', r'\1@' + ref + '/', u) for u in urls]
    failed = 0
    for url in dict.fromkeys(urls):
        try:
            request = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'mandarinmaxxing-check'})
            status = urllib.request.urlopen(request, timeout=30).status
        except Exception as error:  # an HTTP error, a timeout, a refused connection
            status = getattr(error, 'code', None) or str(error)
        ok = status == 200
        failed += not ok
        print(('ok   ' if ok else 'FAIL ') + f'{status}  {urllib.parse.unquote(url)}')
    print(f'{len(dict.fromkeys(urls)) - failed} of {len(dict.fromkeys(urls))} addresses answered')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
