import requests
import bs4

BASEURL = 'https://archiveofourown.org/works/11478249'


def idx(name):
    return int(name[:name.find('.')])


def scrape_chapters():
    req = requests.get(BASEURL)
    soup = bs4.BeautifulSoup(req.text, features='html5lib')
    options = soup.find('select', id='selected_id').find_all('option')
    return [(idx(o.text), o.text, o.attrs['value']) for o in options]


def scrape_chapter(key):
    req = requests.get(f'{BASEURL}/chapters/{key}')
    soup = bs4.BeautifulSoup(req.text, features='html5lib')
    return str(soup.find('div', 'chapter'))


def get_after(prev_idx):
    chaps = [(idx, name, key)
             for (idx, name, key) in scrape_chapters() if idx > prev_idx]

    return [(idx, name, scrape_chapter(key)) for (idx, name, key) in chaps]
