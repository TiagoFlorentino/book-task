# Library task

# Description of the task

API Generation Requirements

### 1 - The library needs to control the entry and exit of books.

The library can support multiple books per title. We need to make sure the books are address by ID on renting and their status is updated based on
their ID instead of title.

### 2 - The library needs to control the state of the books and the person who took them.

The state of the books can be described by the following states:

- AVAILABLE - the book is available to be rented in the library
- RENTED - the book was rented by some active user of the library
- DISCONTINUED - the book is no longer available in the library

If a book is in the rented state - the book entry will contain the ID of the user which has the book
in their possession

### 3 - Track down the library members.

We will be able to list the member of the library by doing a call to the service on /clients.
We will list the status of the user - ```YES or NO``` active status

### 4 - Only active user will be able to rent books

On renting a book, only active users will be able to rent a book. We need to check the status of the user
before allowing the renting process to move forward

### 5 - List the books and their status.

List endpoint will display all the books that were ever available on the library
and their status

# How to use

- Generate your local DB

```poetry run book_task\database\db_init.py```

- Start the API

```poetry run uvicorn main:app --reload```

- Run testing

```poetry run pytest```