# p3-CLI-project

# Library Management System CLI

Welcome to the **Library Management System (LMS) Command-Line Interface (CLI)** project. This system allows users to manage and interact with a library's database, offering options such as browsing available books, borrowing, and returning them.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Database Design](#database-design)

## Project Structure

The project is structured as follows:

```shell
.
├── LICENSE
├── Pipfile and Pipfile.lock
├── README.md
├── lib
│ ├── **init**.py
│ ├── cli.py
│ ├── db
│ │ ├── alembic.ini
│ │ ├── book.sql
│ │ ├── library.db
│ │ ├── migrations
│ │ ├── models.py
│ │ └── session.py
│ ├── helpers.py
│ ├── library.db
│ └── seed.py
├── note.md
└── video
└── VIDEO.md
```

- `cli.py`: Contains the main interface for user interactions with the library.
- `seed.py`: Provides utility functions for seeding the database with sample data.
- `helpers.py`: Contains utility functions for showing available books and handling book borrowing and returning.
- `models.py`: Defines the ORM models for the library's entities.
- `session.py`: Sets up the database session for ORM interactions.
- `db`: Contains database-related files, migrations, and SQL queries.

## Requirements

Ensure you have the following installed:

- Python 3.8 or higher
- `pipenv` for managing dependencies.

## Setup

1. Fork the repository:

2. Install the dependencies:
   ```shell
   pipenv install
   ```
3. Open your virtual environment:
   ```shell
   pipenv shell
   ```
4. Navigate to the lib folder, populate the database with our sample data and kickstart the CLI interface using:
   ```shell
   cd ..
   python seed.py
   python cli.py
   ```

Upon launch:

Login: Input your name to log in. New users are automatically registered.
Exit: Gracefully exit the system.
After logging in, you can:

Browse Available Books: Explore the vast collection in the library.
Borrow a Book: Simply enter the book's ID to borrow.
Return a Book: Return any borrowed book using its ID.
Logout: End your session and revert to the main menu.
Database Design
Our robust database is made of several interconnected tables:

Authors: Information about book authors.
Genres: Distinct book genres.
Books: List of books with references to their respective authors and genres.
Users: Registered system users.
BorrowedBooks: Keeps track of borrowed books and their respective users.
Each table is equipped with relevant attributes, like name, author_id, genre_id, etc. Inter-table relationships are established through foreign keys.

- [Project Requirements](https://my.learn.co/courses/653/pages/phase-3-project-cli?module_item_id=95439)

## Instructions

- Python fundamentals.
- Data structures (and more recently, algorithms).
- Object-oriented programming.
- Object inheritance.
- Class attributes and methods.
- Configuring applications.
- SQL fundamentals.
- Table relations in SQL.
- Object-relational mapping with Python.
- Object-relational mapping with SQLAlchemy.
- Building CLIs.

### The following are the minimum requirements:

- A CLI application that
  - solves a real-world problem
  - adheres to best practices.
- A database created with SQLAlchemy
  - modified with SQLAlchemy ORM
  - 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists.
- Use of dicts.

### Stretch goals:

- Use of additional data structures, such as ranges and tuples.

* A database created and modified with SQLAlchemy ORM with 3+ related tables.
* Use of many-to-many relationships with SQLAlchemy ORM.
