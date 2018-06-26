# coding=utf-8
import requests, re
from bs4 import BeautifulSoup


def get_info_from_url(url):
    """
    Getting info from url in order of elements_to_parse.
    Algorithm will return formatted text if it found it

    :param url: full url to get info
    :return: formatted text
    """
    r = requests.get(url, timeout=2)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    # Order of elemets to parse
    elements_to_parse = ['p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    for i in elements_to_parse:
        el = soup.find(i)

        if el is not None:
            text = el.text
            if text:
                return format_text(text.encode('utf-8'))
    # If nothing found - raising exception
    raise Exception


def format_text(text):
    """Adding trademark symbol to each word in text with length == 6"""

    f_text = re.sub(r'(\b\w{6}\b)', r'\1™', text)

    return f_text.decode('utf-8')


