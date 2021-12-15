import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for i,item in enumerate(items,start=1):
    itemName = item.find('h4',class_='card-title').text.strip()
    itemPrice = item.find('h5').text
    itemLink = 'https://scrapingclub.com' + item.find('a')['href']
    print(f'{i} : {itemName} , {itemPrice}, {itemLink}')