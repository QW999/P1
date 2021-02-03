# comments:
# css selector learning source: https://www.w3schools.com/cssref/css_selectors.asp
# soup objects use css selector sintax with method select - therefore if you would have read the documentation carefully you would have known that already

# problem 1 - resolved partialy. PLease finish it.
import requests
from bs4 import BeautifulSoup
import pprint

site = 'https://hub.packtpub.com/tag/python/'  # the general link to the site


def main(n: int, c: int):
    "This is the function that will get the n and c arguments and will call the needed code writen bellow"
    pass


def iterate_pages(max_page):
    "Iterate the entire range of news pages and return a list of soup objects. Each object representing the respective page content"

    page_list = list()

    for p in range(1, max_page + 1):
        page_link = site + "page/{}/".format(p)
        # print(page_link)
        res = requests.get(page_link)
        soup = BeautifulSoup(res.text, 'html.parser')
        page_list.append(soup)

    return page_list  # return list of tuples


def extract_news(soup_object):
    "Function gets a soup object representing the entire page, then extracts only the news data out of it and packs them in a tuple "

    links = soup_object.select('div[class=td-block-span6] h3 a[rel=bookmark]')
    comments = soup_object.select('div[class=td-module-comments] a')

    news_attr = list()

    for n, comment in zip(links, comments):
        title = n.get('title')
        href = n.get('href')
        c = comment.getText()
        news_attr.append((title, href, c))

    return news_attr  # return list of tuples


def get_page_limit():
    "Get the maximum range of pages that must be iterated. Returns int value"

    res = requests.get(site)
    soup = BeautifulSoup(res.text, 'html.parser')

    pages = soup.select('div span[class=pages]')  # get the element with the max page numbers
    text = pages[0].getText()

    last_character = text.split(' ')[-1]  # isolate the max page number
    return last_character

# news_pages = iterate_pages(2)


