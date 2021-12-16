import requests
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/kirovskaya_oblast_kirov/nedvizhimost?cd=1'

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

items = soup.find_all('div',class_='body-root-c6iTt')

for i, item in enumerate(items,start=1):
    itemName = item.find('h3',class_='title-root-jf957 body-title-TAukq title-root_maxHeight-JYMzC text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text
    itemPrice = item.find('span','price-text-_WjC0 text-text-LurtD text-size-s-BxGpL').text
    itemLink = item.find('a')['href']
    print(f'{i} : {itemName} , {itemPrice} , {itemLink}')