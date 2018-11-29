import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.cricbuzz.com/'

data = requests.get(url)

content = bs(data.content,"html.parser")
print(content)