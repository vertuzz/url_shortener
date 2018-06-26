from flask import Flask
from extensions import db, login_manager
from models import User
from admin import admin


def create_app():

    app = Flask(__name__)

    # setting config
    app.config.from_pyfile('config.py')

    init_extensions(app)

    # registering blueprints
    from frontend import frontend
    from api import api

    app.register_blueprint(frontend)
    app.register_blueprint(api)

    return app


def init_extensions(app):
    db.init_app(app)
    import models
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    admin.init_app(app)

