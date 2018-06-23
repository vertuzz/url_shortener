from extensions import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    url = db.Column(db.String(256), nullable=False)

    short_url = db.Column(db.String(80), nullable=False, unique=True)

    text = db.Column(db.Text)

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)