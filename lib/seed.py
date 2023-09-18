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
