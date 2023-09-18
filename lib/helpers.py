from db.models import Book, BorrowedBook
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


def handle_return_book(user):
    borrowed_books = (
        session.query(BorrowedBook, Book)
        .join(Book, BorrowedBook.book_id == Book.id)
        .filter(BorrowedBook.user_id == user.id)
        .all()
    )
    if not borrowed_books:
        print("\nYou haven't borrowed any books.")
    else:
        print("\nYour Borrowed Books:")
        for record, book in borrowed_books:
            print(f"ID: {book.id}, Name: {book.name}")

        book_id = input("Enter the ID of the book you want to return: ")
        book_record = (
            session.query(BorrowedBook)
            .filter(BorrowedBook.book_id == book_id, BorrowedBook.user_id == user.id)
            .first()
        )
        if book_record:
            book = session.query(Book).filter(Book.id == book_id).first()
            book.is_available = True
            session.delete(book_record)
            session.commit()
            print(f"\nYou've returned {book.name}!")
        else:
            print("\nInvalid choice or you haven't borrowed this book.")
