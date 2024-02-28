# Reviews scrap (box create give correct len)

import pandas as pd
import requests
from bs4 import BeautifulSoup, ResultSet
from pandas import DataFrame

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(
        i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    # product_name(all page)
    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name)
    # print(len(Product_name))

    # prices
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    # print(Prices)

    # Description
    Desc = box.find_all("ul", class_="_1xgFaf")
    for i in Desc:
        name = i.text
        Description.append(name)
    # print(Description)

    # Reviews
    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
        name = i.text
        Reviews.append(name)
    # print(Reviews)
    # print(len(Reviews))

# crate dataframe
a = {"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews}
df = pd.DataFrame.from_dict(a,orient='index')
df = df.transpose()
# print(df)

df.to_csv("C:/Users/rohit/OneDrive/Desktop/vrushali/Scrap Flipkart with python/flipkart_mobiles_under_50000.csv")

# Product_name = []
# Prices = []
# Description = []
# Reviews = []
