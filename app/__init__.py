from flask import Flask
from .db import db, migrate
#from .routes.hello_world_routes import hello_world_bp
from .routes.book_routes import books_bp
from .models import book # Newly added import
import os

def create_app(config=None):
    app = Flask(__name__)
    #app.register_blueprint(hello_world_bp)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)

    return app