# Endpoints


## Book Operations

### GET - /list_books

Description: list all the books in the library

### POST - /add_book

Description: Add a book to the library

```json
{
  "title": "The Waking Hours"
}
```

### GET - /search_book

Description: Search a book by title or ID

Examples:

- by ID
    ```json
    {
      "id": 1
    }
    ```

- by Name
    ```json
    {
      "title": "BITS BITS"
    }
    ```

### POST - /rent_book

Description: Rent a book from the library (if available)

```json
{
  "book_id": 1,
  "client_id": 1
}
```

### POST - /book_status

Description: Change the status of a book in the library. Cannot change a status of a book
to rented using this operation

All Status: 
- 
- AVAILABLE - the book is available to be rented in the library
- RENTED - the book was rented by some active user of the library. Status not available in this operation
- DISCONTINUED - the book is no longer available in the library

```json
{
  "id": 1,
  "status": "AVAILABLE" // or "DISCONTINUED"
}
```
