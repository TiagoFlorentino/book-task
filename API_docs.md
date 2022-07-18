# Endpoints

## Client Operations

### GET - /list_clients

Description: list the clients on the library

### POST - /search_client

Description: Search a client by name or ID

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
      "name": "JOSE ANTONIO"
    }
    ```

### POST - /client_status

Description: Activate or Deactivate a client by ID

Examples:

```json
{
  "id": 1,
  "active": "TRUE" (or FALSE)
}
```


### POST - /add_client

Description: Create a new client to the library

Example:

```json
{
  "name": "JOSE ANTONIO"
}
```

## Book Operations

### GET - /list_books

Description: list all the books in the library

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
- RENTED - the book was rented by some active user of the library
- DISCONTINUED - the book is no longer available in the library

```json
{
  "id": 1,
  "status": 1
}
```
