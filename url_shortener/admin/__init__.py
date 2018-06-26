from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from url_shortener.models import db, Urls

admin = Admin()

admin.add_view(ModelView(Urls, db.session))