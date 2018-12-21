import subprocess


def ebook_convert(src_file, mobi_name, name, author):
    subprocess.run(['ebook-convert',
                    src_file,
                    mobi_name,
                    '--title', name,
                    '--authors', author,
                    ])


def send_ebook(src, pw, dst, attachment):
    subprocess.run(['sendemail',
                    '-f', src,
                    '-t', dst,
                    '-u', 'subject',
                    '-m', 'body',
                    '-s', 'smtp.gmail.com:587',
                    '-o', 'tls=yes',
                    '-a', attachment,
                    '-xu', src,
                    '-xp', pw,
                    ], check=True)
