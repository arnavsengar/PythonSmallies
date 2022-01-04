import requests
from bs4 import BeautifulSoup
s="Weather in "+input("Enter City: ")
u=f"https://www.google.com/search?&q={s}"
r=requests.get(u)
s=BeautifulSoup(r.text,"html.parser")
update=s.find("div",class_="BNeawe").text
print(update)