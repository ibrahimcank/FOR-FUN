import requests

from bs4 import BeautifulSoup
url="https://yellowpages.com.tr/ada-bilgisayar-laptop-hastanesi-merkez-karaman"

response= requests.get(url)
html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")
print(soup.prettify())

print(soup.find_all("a"))
 #site içinden sadece linkleri alır
for i in soup.find_all("a"):
     print(i.get("href")) 
 # a etiketi içindeki yazıları almak için
for i in soup.find_all("a"):
     print(i.text) 

print(soup.find_all("div",{"class":"yp-poi-box-2"}))