from db.models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///library.db")

Session = sessionmaker(bind=engine)
session = Session()


class Cli:
    def __init__(self):
        self.current_user = None
