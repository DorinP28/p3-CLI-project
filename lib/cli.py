from db.models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///library.db")

Session = sessionmaker(bind=engine)
session = Session()


class Cli:
    def __init__(self):
        self.current_user = None

    def start(self):
        print("Welcome to the Library Management System!")
        options = ["Login", "Exit"]
        terminal_menu = TerminalMenu(options)

        while True:
            menu_entry_index = terminal_menu.show()
            if options[menu_entry_index] == "Login":
                self.handle_login()
                self.handle_user_actions()
            else:
                self.exit()
