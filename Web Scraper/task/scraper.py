import requests
import os

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
    title = parsed.find(class_="article-item__title").string
    print(f"Done! {title}")
    return title


def get_article_text(page):
    """get article text"""
    parsed = BeautifulSoup(page, 'html.parser')
    print("Getting article text...")
    text = parsed.find(class_="article__body u-clearfix")
    if not text:
        text = parsed.find(class_="article-item__body")
    print(f"Done! {text}")
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


def create_folder(page_number):
    """creates a folder with Page_N name"""
    print(f"Creating folder with Page_{page_number} name...")
    try:
        os.mkdir(f"Page_{page_number}")
        print("Done!")
    except FileExistsError:
        print("Folder already exists, continue...")
        return True


def change_saving_directory(directory_name):
    """changes current working directory to directory name"""
    print(f"Changing working directory to {directory_name}...")
    os.chdir(directory_name)
    print(f"Done, we are in {os.getcwd()}")


starting_url = 'https://www.nature.com/nature/articles/?searchType=journalSearch&sort=PubDate&page='
page_count = int(input())
article_type = input()
base_folder = os.getcwd()

for page_num in range(1, page_count + 1):
    create_folder(page_num)
    change_saving_directory(f"Page_{page_num}")
    r = get_page_content(starting_url + str(page_num))
    soup = BeautifulSoup(r, 'html.parser')
    all_articles = soup.find_all('article')
    for article in all_articles:
        if article.find(class_="c-meta__type").string == article_type:
            article_href = article.find(attrs={'data-track-action': 'view article'}).get('href')
            url = f"https://www.nature.com{article_href}"
            print("-------------------------------------------")
            page_content = get_page_content(url)
            article_title = get_article_title(page_content)
            article_text = str(get_article_text(page_content)).strip()
            file_name = prepare_file_name(article_title)
            save_file(file_name, article_text)
    change_saving_directory(base_folder)

print("Saved all articles.")





