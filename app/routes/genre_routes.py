from flask import Blueprint, request
from app.models.book import Book
from app.models.genre import Genre
from .route_utilities import create_model, get_models_with_filters, validate_model

genres_bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@genres_bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)

@genres_bp.get("")
def get_all_genres():
    return get_models_with_filters(Genre, request.args)

@genres_bp.post("/<genre_id>/books")
def create_book_with_genre(genre_id):
    genre = validate_model(Genre, genre_id)

    request_body = request.get_json()
    request_body["genres"] = [genre]
    return create_model(Book, request_body)

@genres_bp.get("/<genre_id>/books")
def get_books_by_genre(genre_id):
    genre = validate_model(Genre, genre_id)
    response = [book.to_dict() for book in genre.books]
    return response