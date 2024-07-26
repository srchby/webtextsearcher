import requests
import html2text as h2t
from bs4 import BeautifulSoup

# Insert your url
url = ""
requrl = requests.get(url)

html = requrl.text

h = h2t.HTML2Text()
h.ignore_links = True
mdtxt = h.handle(html)

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string.strip() if soup.title else "No title found"

def valid_filename(title):
    chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in chars:
        title = title.replace(char," ")
    return title

filename = valid_filename(title)

filetxt = open(f'{filename}.md','w')
filetxt.write(mdtxt)
filetxt.close()
