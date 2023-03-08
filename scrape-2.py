import requests
from bs4 import BeautifulSoup

url = "https://www.standardmedia.co.ke"

reponse = requests.get(url)

# print(reponse.status_code)

soup = BeautifulSoup(reponse.content, "html.parser")

story_titles = soup.find("div", class_="sub-title mb-2")

# story_titles = story_titles.find('p')

print(story_titles)

# for title in story_titles:
#     print(title.text)

