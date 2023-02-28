import requests

data = {'name': 'John', 'age': 30}

response = requests.post('https://httpbin.org/post', data=data)

# print(response.status_code)
# print(response.content)

# response = requests.get('https://api.github.com')

# print(response.status_code)

# print(response.content)

# text = 'Hello, world!'
# bytes = text.encode('utf-8')
# print(bytes)

import urllib.request

url = 'https://api.github.com'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
print(text)
