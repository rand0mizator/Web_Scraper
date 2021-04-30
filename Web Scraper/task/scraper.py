import requests
from bs4 import BeautifulSoup
from string import punctuation


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
    print("Done!")
    return title


def get_article_text(page):
    """get article text"""
    parsed = BeautifulSoup(page, 'html.parser')
    print("Getting article text...")
    text = parsed.find(class_="article__body cleared")
    print("Done!")
    return text.get_text()


def prepare_file_name(title):
    """Replace the whitespaces with underscores and remove punctuation marks in the filename
    (str.maketrans and string.punctuation will be useful for this). Also, strip all trailing whitespaces
     in the article title"""
    stripped_title = str(title).strip()
    trans_table = stripped_title.maketrans(' ', '_', punctuation)  # swap "space" with "undescore", "punctuation" with None
    return stripped_title.translate(trans_table) + '.txt'


def save_file(title, text):
    """saves file with article_title and article_text"""
    print("Saving to file")
    file = open(title, 'w', encoding='utf-8')
    file.write(text)
    file.close()
    print(f"File saved {title}")


urls = []
starting_url = 'https://www.nature.com/nature/articles/'
r = get_page_content(starting_url)
soup = BeautifulSoup(r, 'html.parser')
all_articles = soup.find_all('article')
for article in all_articles:
    if article.find(class_="c-meta__type").string == 'News':
        article_href = article.find(attrs={'data-track-action': 'view article'}).get('href')
        urls.append(f"https://www.nature.com{article_href}")

print(urls)
for url in urls:
    print("-------------------------------------------")
    page_content = get_page_content(url)
    article_title = get_article_title(page_content)
    article_text = str(get_article_text(page_content)).strip()
    file_name = prepare_file_name(article_title)
    save_file(file_name, article_text)





