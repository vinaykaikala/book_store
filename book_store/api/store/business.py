from book_store.database import db
from book_store.database.models import BookStore as books_table

def get_books():
    "List all books available in the store"
    return  books_table.query.all(), 200
