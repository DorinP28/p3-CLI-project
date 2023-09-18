from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Author, Book, User
from faker import Faker

engine = create_engine("sqlite:///library.db")

fake = Faker()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_authors(num_authors=5):
    authors = []
    for _ in range(num_authors):
        author = Author(name=fake.name())
        session.add(author)
        authors.append(author)
    session.commit()
    return authors


def create_users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User(name=fake.name())
        session.add(user)
        users.append(user)
    session.commit()
    return users


def create_books(authors):
    book_titles = [
        lambda: fake.catch_phrase(),
        lambda: fake.bs(),
        lambda: f"{fake.color_name()} {fake.word()}",
        lambda: f"{fake.city()} {fake.word()}",
        lambda: fake.job(),
    ]
    min_books_per_author = 1
    max_books_per_author = 5

    books = []
    for author in authors:
        num_books = random.randint(min_books_per_author, max_books_per_author)
        for _ in range(num_books):
            title = random.choice(book_titles)()
            title = " ".join(word.capitalize() for word in title.split())
            book = Book(name=title, author_id=author.id, is_available=True)
            session.add(book)
            books.append(book)
    session.commit()
    return books


if __name__ == "__main__":
    authors = create_authors()
    books = create_books(authors)
    users = create_users()
    print(f"Seeded {len(authors)} authors, {len(books)} books, and {len(users)} users.")
