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

### 6 - Joining a new campaign.

The client can join a new campain at any time. New users will  be registered as new users
by the campaign if they have registered in the last hour.

### 7 - Tracking book logs

The library keeps a list of all the users how rented a book.

### 7 - Partners are the campaign's sponsor

From time to time the library has active campaigns which are sponsored by a 
partner. We can list the active period of each partner given their status change.


# How to start the project

- Generate your local DB

```poetry run python book_task\database\db_init.py```

- Start the API

```poetry run uvicorn main:app --reload```

- Run React APP on a separate terminal

```cd frontend\library```

```npm start```


# How to run testing

```poetry run pytest```


# Front End Endpoints Help Guide

## Add operations

```add_client``` -> Add a new client

```add_book``` -> Add a new book

```add_partner``` -> Add a new partner

```add_campaign``` -> Add a new campaign

## List Operations

```list_books``` -> List the books of the library

```list_campaigns``` -> List the campaigns of the library

```list_clients``` -> List the clients of the library

```list_partners``` -> List the partners of the library

## Search Operations

```search_book``` -> List the renting operations done on a book

```search_campaign``` -> List the users who joined a campaign

```search_partner``` -> List the status changes of a partner

## Action operations

```rent_book``` -> Rent a book from the library

```join_campaign``` -> A client can join a campaign