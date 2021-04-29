import requests
from bs4 import BeautifulSoup

urls = []
starting_url = 'https://www.nature.com/nature/articles'
r = requests.get(starting_url)
status_code = r.status_code
soup = BeautifulSoup(r.content, 'html.parser')
all_headers = soup.find_all(attrs={'data-track-action': 'view article'})
print(all_headers)
for header in all_headers:
    urls.append(f"https://www.nature.com{header.get('href')}")
print(urls)


def get_title(url):
    pass


def get_content(url):
    pass


def prepare_content(text):
    pass


def save_file(file_name, content):
    pass
