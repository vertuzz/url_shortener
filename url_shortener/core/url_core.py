import random, string
from flask import abort
from ..models import db, Urls


def generate_short_url(domain=None):
    domain = domain if domain else 'http://domain.com/'
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
    return domain + rand


def save_url(url, domain=None):
    short_url = generate_short_url(domain=domain)
    r = Urls(url=url, short_url=short_url)
    db.session.add(r)
    db.session.commit()

    return short_url


def url_to_redirect(domain, short_url):
    res = Urls.query.filter_by(short_url=domain+short_url).first()
    if res is None:
        abort(404)
    res.clicked = res.clicked + 1
    db.session.commit()
    url = res.url
    if 'http://' not in url or 'https://' not in url:
        url = 'http://' + url
    return url
