# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup
import re


def crawling(url):  # 크롤링 사이트서 문장추출
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    sentence = soup.find('div', attrs={"class":
                                           "article__content"}).get_text()
    return sentence


def to_word(sentence):  # 문장을 단어로

    new_sen = re.sub(r"[^a-z\s]", "", sentence)  # 특수기호 제거

    words = new_sen.split()  # 문장을 리스트로
    words = list(set(words))  # 중복 제거

    return words


def extract_word(url):  # 크롤링 사이트에서 단어추출
    sentence = crawling(url)
    words = to_word(sentence)

    return words


if __name__ == "__main__":
    # url = "https://edition.cnn.com/2022/12/17/europe/moscow-army-recruits-intl/index.html"
    url = "https://edition.cnn.com/2022/12/16/opinions/germany-plot-overthrow-government-prince-weber/index.html"

    extract_word(url)


