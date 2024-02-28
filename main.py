# data can be obtain inside page

import pandas as pd
import requests
from bs4 import BeautifulSoup


for i in range(2,10):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text,"lxml")
    # print(soup)


     # while True:
    np = soup.find("a",class_="_1LKTO3").get("href")
    cnp = "https://www.flipkart.com"+np
    print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")




