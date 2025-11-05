from flask import Flask
from .db import db, migrate
#from .routes.hello_world_routes import hello_world_bp
from .routes.book_routes import books_bp
from .routes.author_routes import authors_bp
from .models import book, author # Newly added import
import os

def create_app(config=None):
    app = Flask(__name__)
    
    # Database configuration - prefer SQLALCHEMY_DATABASE_URI over DATABASE_URL
    database_url = os.getenv('SQLALCHEMY_DATABASE_URI') or os.getenv('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        # Fix Render's postgres:// style URLs to work with SQLAlchemy
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or \
        'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)

    return app