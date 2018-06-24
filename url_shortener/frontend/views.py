from flask import Blueprint, render_template, redirect, request
from url_shortener.core.url_core import url_to_redirect

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/<short_url>')
def url_redirect(short_url):
    url = url_to_redirect(request.url_root , short_url)
    return redirect(url, code=302)
