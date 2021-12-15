# https://habr.com/ru/sandbox/151294/

import requests
from bs4 import BeautifulSoup

url = "http://militera.lib.ru/1/cats/all/a/index.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

soup = soup.encode()

with open('test.html', 'wb') as file:
    file.write(soup)