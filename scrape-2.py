import requests
from bs4 import BeautifulSoup

url = "https://www.goojara.to/"

reponse = requests.get(url)

# print(reponse.status_code)

soup = BeautifulSoup(reponse.content, "html.parser")

movie_titles = soup.find_all("div")

for title in movie_titles:
    print(title.content)

