import requests
from bs4 import BeautifulSoup
import csv

url = "https://hojaleaks.com/series/python"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

headings = soup.find_all('h1', class_='blog-post-card-title css-1x2fmqg')
# mini_headings = soup.find_all('h2', class_='entry-title')

for heading in headings:
    print(heading.text)
    
with open('headings.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Headings'])
    for heading in headings:
        writer.writerow([heading.text])
