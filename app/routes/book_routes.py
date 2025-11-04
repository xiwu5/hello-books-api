from flask import Blueprint, Response, abort, make_response, request
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
#from app.models.book import books
from app.models.book import Book
from ..db import db


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)

@books_bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)

@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()

# def validate_book(cls, book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         response = {"message": f"{cls.__name__} {book_id} invalid"}
#         abort(make_response(response , 400))

#     query = db.select(cls).where(cls.id == book_id)
#     book = db.session.scalar(query)

#     if not book:
#         response = {"message": f"{cls.__name__} {book_id} not found"}
#         abort(make_response(response, 404))

#     return book

@books_bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")