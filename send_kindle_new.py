import html
import os
import sys
import time

import scraper
import kindle

EMAIL_CREDENTIALS = 'EMAIL_CREDENTIALS'

AUTHOR = 'cthuluraejepsen'

HTML_FILE = 'CHAPTER.html'

PREV = 'previous'


def email_creds():
    with open(EMAIL_CREDENTIALS) as f:
        return list(map(str.strip, f.readlines()))


def html_encode_unicode(text):
    return ''.join(
        c if ord(c) < 128 else '&#{};'.format(ord(c))
        for c in text)


def format_chapter(title, text):
    TEMPLATE = '''
    <DOCTYPE html>
    <html lang="en">
    <head>
        <title>{title}</title>
        <meta name="author" content="{author}"></meta>
    </head>
    <body>
        <h3>{title}</h3>
        <div align="left">
        {text}
        </div>
    </body>
    </html>
    '''

    escaped = html_encode_unicode(text)
    return TEMPLATE.format(author=AUTHOR, title=title, text=escaped)


def send_chapters_since(prev):
    uname, pw, dest = email_creds()

    chapters = scraper.get_after(prev)

    print('%d new chapters' % len(chapters))

    latest = 0
    for idx, name, content in chapters:
        print('Sending %s to %s from %s' % (name, dest, uname))

        formatted = format_chapter(name, content)
        fname = f'{name}.html'
        with open(fname, 'w') as f:
            f.write(formatted)

        kindle.send_ebook(uname, pw, dest, fname)

        latest = max(idx, latest)

    return latest


def get_latest():
    with open(PREV) as f:
        return int(f.read())


def update_latest(idx):
    with open(PREV, 'w') as f:
        f.write(f'{idx}\n')


def main():
    pidx = get_latest()
    nidx = send_chapters_since(pidx)
    update_latest(nidx)


if __name__ == '__main__':
    main()
