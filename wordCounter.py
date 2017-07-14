import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)

    for a in soup.findAll('a',{'class':'index_img'}):
        content = a.string
        words = content.lower().split()

        for each_word in words:
            word_list.append(each_word)
