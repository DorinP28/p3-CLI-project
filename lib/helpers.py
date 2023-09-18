from db.models import Book
from db.session import Session

session = Session()


def show_available_books():
    available_books = session.query(Book).filter(Book.is_available == True).all()
    if not available_books:
        print("\nNo books available at the moment.")
    else:
        print("\nAvailable Books:")
