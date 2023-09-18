from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Author, Book, User

engine = create_engine("sqlite:///library.db")
