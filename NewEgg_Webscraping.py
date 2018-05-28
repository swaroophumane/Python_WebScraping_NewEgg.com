from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

my_url = 'https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&ignorear=0&N=-1&isNodeId=1'

# Opening up connection and grabbing the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
# print(page_soup.prettify())

# print(page_soup.h1.text)  # Retriving h1 tag and inside text
# print(page_soup.p.text)  # Retriving p tag and inside text

containers = page_soup.findAll('div', {'class': 'item-container'})

filename = 'Products.csv'

with open(filename, 'w') as f:
    headers = 'Brand , Product Title, Price\n'
    f.write(headers)
    for container in containers:
        try:
            brand = container.find('a', {'class': 'item-brand'}).img['title']
            title_container = container.find('a', {'class': 'item-title'}).text
            price = container.find(
                'li', {'class': 'price-current'}).text[4:].strip()
            price = re.findall(r'([\d,]+)', price)
            print("Brand", brand)
            print("Title_container", title_container)
            print("Price", price[0])

            f.write(brand.replace(",", '') + ',' +
                    title_container.replace(",", "~") + ',' + price[0].replace(",", "") + "\n")
        except:
            continue
