import requests
from bs4 import BeautifulSoup

headers = {'Accept-Language': 'en-US,en;q=0.5'}
output = dict()

url = input()

r = requests.get(url, headers=headers)
html_doc = r.content
soup = BeautifulSoup(html_doc, 'html.parser')
p = soup.find('div', {'class': 'summary_text'})

try:
    output['title'] = soup.title.string
    output['description'] = p.string
    print(output)
except AttributeError:
    print('Invalid movie page!')
