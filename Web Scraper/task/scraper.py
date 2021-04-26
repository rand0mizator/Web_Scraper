import requests
from bs4 import BeautifulSoup

data = {}

url = 'https://www.nature.com/nature/articles'
r = requests.get(url)
status_code = r.status_code
soup = BeautifulSoup(r.content, 'html.parser')
all_headers = soup.find_all('h3')
for header in all_headers:
    print(f"{header.a.string} - https://www.nature.com/nature{header.a['href']}")

