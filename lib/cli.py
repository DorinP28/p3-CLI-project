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

    def handle_login(self):
        username = input("\nEnter your name: ")
        user = session.query(User).filter(User.name == username).first()
        if user:
            self.current_user = user
            print(f"\nWelcome back, {user.name}!")
        else:
            self.current_user = User(name=username)
            session.add(self.current_user)
            session.commit()
            print(f"\nWelcome, {self.current_user.name}!")

    def handle_user_actions(self):
        while True:
            print("\nChoose an action:")
            options = [
                "Browse Available Books",
                "Borrow a Book",
                "Return a Book",
                "Logout",
            ]
            terminal_menu = TerminalMenu(options)
            choice = options[terminal_menu.show()]

            if choice == "Browse Available Books":
                show_available_books()
            elif choice == "Borrow a Book":
                handle_borrow_book(self.current_user)
            elif choice == "Return a Book":
                handle_return_book(self.current_user)
            elif choice == "Logout":
                break

    def exit(self):
        print("\nThank you for using the Library Management System!")
        quit()
