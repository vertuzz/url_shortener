# coding=utf-8
import requests, re
from bs4 import BeautifulSoup


def get_info_from_url(url):
    r = requests.get(url, timeout=2)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    elements_to_parse = ['p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    el = None
    text = None

    for i in elements_to_parse:
        el = soup.find(i)

        if el is not None:
            return format_text(el.text.encode('utf-8'))

    raise Exception


def format_text(text):

    f_text = re.sub(r'(\b\w{6}\b)', r'\1™', text)

    return f_text.decode('utf-8')


