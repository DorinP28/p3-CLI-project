## Main idea:

### Library Management System - A CLI application for readers to browse available books in a library and borrow or return them.

## User story:

- Users will browse through a list of available books and their details.
- Users will borrow a book, marking it as "borrowed" in the system.
- Users can view details of a specific book.
- Users can see their list of borrowed books.
- Users can return a borrowed book.

How I will use the concepts I recently learned to meet the project requirements:

- Object Oriented Python

  - Class for `Book` with attributes like title, author, ISBN, and status (available/borrowed).
  - Class for `Reader` with attributes like name, membership ID, and list of borrowed books.

- Database Tables
  - Table: `Readers`
    - id
    - name
    - email
  - Table: `Books`
    - id
    - title
    - author
    - ISBN
    - status
  - Table: (many to many) `Reader-Book` =="List of borrowed books"
    - id
    - book id
    - reader id who borrowed the book
- Object Relationships

  - Reader can borrow many books.
  - A Book can be borrowed by many readers over its lifetime.
  - Readers to Book - many to many
    - with join table `reader-borrowed-book`

- Aggregate and Association Methods

  - CRUD
    - Create
      - Mark a book as borrowed.
    - Read
      - Display all available books.
      - Display borrowed books by a reader.
      - View a book's details by ID.
    - Update
      - Mark a book as returned.
    - Delete
      - Remove a book from the system (in case of loss or damage).

- Use of Data Structures
  - Single Source of Truth
  - List: Reader could have a list of book IDs they've borrowed.
  - Dictionary: Each book has a set of attributes and their corresponding values.

### What area I think will be most challenging:

- Implementing the logic to update the book's status (available/borrowed) in real-time and ensuring that the borrow and return actions are accurately logged in the system.

---

---

---

---

## Second Idea:

### Hotel Booking System - A CLI application for travelers to browse available rooms in a hotel and make reservations.

## User story:

- Users will browse through a list of available rooms with their details (type, view, amenities).
- Users will make a reservation for a specific room for chosen dates.
- Users can view details of a specific room.
- Users can see their active and past reservations.
- Users can cancel an active reservation.

How I will use the concepts I recently learned to meet the project requirements:

- Object Oriented Python

  - Class for `Room` with attributes like room number, type (single, double, suite), view (sea, city, garden), amenities, and reservation status.
  - Class for `Guest` with attributes like name, ID, and list of reservations.

- Database Tables
  - Table: `Guests`
    - id
    - name
    - email
  - Table: `Rooms`
    - id
    - room number
    - type
    - view
    - amenities
    - reservation status
  - Table: `Reservations`
    - id
    - room id
    - guest id
    - check-in date
    - check-out date
- Object Relationships

  - A Guest can make multiple reservations.
  - A Room can be reserved by many guests over its lifespan, but only one guest at a time.
  - Guest to Room - many to one (within the context of a reservation)

- Aggregate and Association Methods

  - CRUD
    - Create
      - Make a new reservation.
    - Read
      - Display all available rooms.
      - Display active and past reservations of a guest.
      - View a room's details by its ID.
    - Update
      - Cancel an active reservation.
      - Modify reservation dates.
    - Delete
      - Remove a reservation (after check-out or cancellation).

- Use of Data Structures
  - Single Source of Truth
  - List: Guests could have a list of room IDs they've reserved.
  - Dictionary: Each room has a set of attributes and their corresponding values.

### What area I think will be most challenging:

- Managing availability and ensuring that double bookings do not occur. Handling the logic when the same room is requested by multiple users for overlapping dates.
