import requests
import html2text as h2t
from bs4 import BeautifulSoup

url = "https://produto.mercadolivre.com.br/MLB-4694307296-notebook-lenovo-core-i5-16gb-ram-256gb-ssd-windows-11-pro-_JM?searchVariation=180512720468#searchVariation%3D180512720468%26position%3D18%26search_layout%3Dgrid%26type%3Ditem%26tracking_id%3D5cc68801-3b1c-4286-a54d-f29b8cf0a649"
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
