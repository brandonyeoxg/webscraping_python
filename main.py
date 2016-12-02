__Author__ = "Brandon Yeo"

import requests
from bs4 import BeautifulSoup

def crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://sg.carousell.com/categories/electronics-gadgets-7?page=" + str(page)
        sourceCode = requests.get(url)
        plain_text = sourceCode.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('h4',{'class': 'pdt-card-title'}):
            value = link.string
            print(value)
        page+=1

crawler(1)