from lxml import html
import requests
from bs4 import BeautifulSoup

#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
tree = html.fromstring(page.content)  # this gets and transforms data in byte form (i.e. not text)

#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print('Buyers:', buyers)
#print('Prices:', prices)


soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

print(list(soup.children))

soup.find_all('p', class_='outer-text')




