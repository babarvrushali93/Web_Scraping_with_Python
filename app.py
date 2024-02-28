# data scraping
from typing import Any

import pandas as pd
import requests
from bs4 import BeautifulSoup, ResultSet

Product_name = []
Prices = []
Description = []
Reviews = []
Ratings = []

url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)

r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,"lxml")


# product_name(all page)
names = soup.find_all("div",class_="_4rR01T")
for i in names:
    name = i.text
    Product_name.append(name)

print(Product_name)
# print(len(Product_name))

# prices

prices = soup.find_all("div",class_="_30jeq3 _1_WHN1")

for i in prices:
    name = i.text
    Prices.append(name)
print(Prices)

# Description
Desc = soup.find_all("ul",class_="_1xgFaf")
for i in Desc:
    name = i.text
    Description.append(name)
print(Description)

# Reviews
reviews = soup.find_all("div", class_="_3LWZlK")
for i in reviews:
    name = i.text
    Reviews.append(name)
print(Reviews)
# print(len(Reviews))


















    # print(soup)


     # while True:
    # np = soup.find("a",class_="_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)
