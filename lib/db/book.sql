SELECT 
    books.name AS book_name, 
    authors.name AS author_name
FROM books
JOIN authors ON books.author_id = authors.id;