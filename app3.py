# data can be obtain inside page

import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,10):
    url = "https://www.flipkart.com/search?q=watch+for+women&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_sc_na_na&as-pos=3&as-type=RECENT&suggestionId=watch+for+women%7CWrist+Watches&requestId=99d228d0-d7e4-46fc-8176-c719643ff531&as-searchtext=wiatch&page=" + str(
        i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    # box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    # product
    names = soup.find_all("div", class_="_2WkVRV")
    for i in names:
        name = i.text
        Product_name.append(name)
    print(Product_name)
    print(len(Product_name))

    # prices
    prices = soup.find_all("div", class_="_30jeq3")
    for i in prices:
        name = i.text
        Prices.append(name)
    print(Prices)

    # Description
    Desc = soup.find_all("a", class_="IRpwTa")
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
    print(len(Reviews))
a = {"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df)

df.to_csv("C:/Users/rohit/OneDrive/Desktop/vrushali/Scrap Flipkart with python/flipkart_watch_for_women.csv")



