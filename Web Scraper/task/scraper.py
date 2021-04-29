import requests
from bs4 import BeautifulSoup


def get_page_content(url):
    """requests all page content by url"""
    print(f"Requesting page content by URL: {url}")
    request = requests.get(url)
    if request.status_code != 200:
        print(f"Something went wrong, error: {request.status_code}")
        return False
    else:
        print("Done!")
        return request.content


def get_article_title(page):
    """return article title"""
    parsed = BeautifulSoup(page, 'html.parser')
    print("Getting article title...")
    title = parsed.title.string
    if title:
        print(f"Done!\nTitle: {title}\n")
        return title
    else:
        print(f"Something went wrong, title = {title}")
        return False


def get_article_text(page_content):
    """get article text"""
    soup = BeautifulSoup(page_content, 'html.parser')
    print("Getting article text...")
    # text = (soup.find(attrs={'class': 'article-item__teaser-text'}).string).strip()
    text = soup.find(class_="article-item__body")
    for row in text.find_all('p'):
        print(row.string)


    # if text:
    #     print(f"Done!\nArticle text: {text}\n")
    #     return text
    # else:
    #     print(f"Something went wrong, text = {text}")
    #     return False

def prepare_text(article_text):
    """strip all trailing whitespaces in article text"""
    pass


def prepare_file_name(article_title):
    """Replace the whitespaces with underscores and remove punctuation marks in the filename
    (str.maketrans and string.punctuation will be useful for this). Also, strip all trailing whitespaces
     in the article title"""
    pass


def save_file(article_title, article_text):
    """saves file with article_title and article_text"""
    pass


urls = []
starting_url = 'https://www.nature.com/nature/articles'
r = get_page_content(starting_url)
soup = BeautifulSoup(r, 'html.parser')
all_headers = soup.find_all(attrs={'data-track-action': 'view article'})
# print(all_headers)
for header in all_headers:
    urls.append(f"https://www.nature.com{header.get('href')}")
# print(urls)

for url in urls[:1]:
    page_content = get_page_content(url)
    article_title = get_article_title(page_content)
    article_text = get_article_text(page_content)




