from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Author, Book, User
from faker import Faker

engine = create_engine("sqlite:///library.db")

fake = Faker()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
