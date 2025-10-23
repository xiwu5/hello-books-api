from flask import Flask
from .db import db, migrate
#from .routes.hello_world_routes import hello_world_bp
from .routes.book_routes import books_bp
from .models import book # Newly added import

def create_app():
    app = Flask(__name__)
    #app.register_blueprint(hello_world_bp)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)

    return app