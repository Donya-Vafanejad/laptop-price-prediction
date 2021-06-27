import re
import requests
from bs4 import BeautifulSoup
import csv
from sklearn import tree
prices=[]
post_models = []
ram = []
memory = []
pardazande = []
new_urls = []
post__urls=[]
monitor=[]
ids=[]
l=[]
y=[]


url = "https://www.digikala.com/search/category-notebook-netbook-ultrabook/?q=laptop"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")



post_url = soup.find_all("a",class_="js-product-url")
for model in post_url:
      post__urls.append(model["href"])

for item in post__urls:
   new_url="https://www.digikala.com"+item
   new_urls.append(new_url)
soups=[]
x=len(new_urls)



for i in range(0,20):
   page = requests.get(new_urls[i])
   soup = BeautifulSoup(page.text, "html.parser")
   model = soup.find('div', class_='c-product__params js-is-expandable')

   ram.append(model)
   info = list(model.text.split())
   pardazande.append(info[24])
   memory.append(info[3])
   monitor.append(info[17])
   price= soup.find('div', class_='c-product__seller-price-raw js-price-value')
   price=price.text.split()
   prices.append(price[0])
   id=soup.find('h1', class_='c-product__title')
   id=id.text.strip()
   ids.append(id)

row_list=list(zip(ids,memory,monitor,prices))


with open("final_web.csv", "w", newline="", encoding="utf-8") as f:
   writer = csv.writer(f)
   writer.writerows(row_list)

with open("final_web.csv", "r") as r_file:
   data = csv.reader(r_file)
   for line in data:
      l.append(line[1:3])
      y.append(line[3])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(l,y)

new_data  = [[4,11.6],[8,15.6]]

answer= clf.predict(new_data)

print(l)
print(y)
print(answer)

#I tried to go with x=len(new_urls) but it crashes, I think Farsi digits cause a problem I can't read it in my copmuter. please help I just have a few days until the end of class. Thanks
pip3 install beautifulsoup4