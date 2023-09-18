from db.models import Book
from db.session import Session

session = Session()


def show_available_books():
    available_books = session.query(Book).filter(Book.is_available == True).all()
    if not available_books:
        print("\nNo books available at the moment.")
    else:
        print("\nAvailable Books:")
        for book in available_books:
            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author.name}")


def handle_borrow_book(user):
    show_available_books()
    book_id = input("Enter the ID of the book you want to borrow: ")
    book = (
        session.query(Book)
        .filter(Book.id == book_id, Book.is_available == True)
        .first()
    )
    if book:
        book.is_available = False
        borrowed_book = BorrowedBook(user_id=user.id, book_id=book.id)
        session.add(borrowed_book)
        session.commit()
        print(f"\nYou've borrowed {book.name}!")
    else:
        print("\nInvalid choice or book not available.")
