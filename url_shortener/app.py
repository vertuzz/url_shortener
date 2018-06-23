from flask import Flask
from extensions import db


def create_app():

    app = Flask(__name__)

    # setting config
    app.config.from_pyfile('config.py')

    # init extensions
    db.init_app(app)
    import models

    # registering blueprints
    from frontend import frontend
    from api import api

    app.register_blueprint(frontend)
    app.register_blueprint(api)

    return app
