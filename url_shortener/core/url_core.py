import random, string
import threading
from flask import abort, copy_current_request_context
from ..models import db, Urls
from parse_core import get_info_from_url


def generate_short_url(domain=None):
    domain = domain if domain else 'http://domain.com/'
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
    return domain + rand


def save_url(url, domain=None):

    if 'http://' not in url or 'https://' not in url:
        url = 'http://' + url

    short_url = generate_short_url(domain=domain)
    r = Urls(url=url, short_url=short_url)
    db.session.add(r)
    db.session.commit()

    @copy_current_request_context
    def save_info_async(row_id, url):
        info = get_info_from_url(url)
        row = Urls.query.get(row_id)
        row.text = info
        db.session.commit()

    th = threading.Thread(target=save_info_async, args=(r.id, url,))
    th.start()

    return short_url




def url_to_redirect(domain, short_url):
    res = Urls.query.filter_by(short_url=domain+short_url).first()
    if res is None:
        abort(404)
    res.clicked = res.clicked + 1
    db.session.commit()
    url = res.url
    return url
