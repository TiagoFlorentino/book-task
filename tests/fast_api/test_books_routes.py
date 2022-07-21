import json
import pytest
from main import database


@pytest.mark.asyncio
async def test_get_books(fast_api_test_client):
    """
    Test the list operations for books
    """
    test_book_list = [
        {"title": "BOOK_1", "status": "AVAILABLE"},
        {"title": "BOOK_2", "status": "RENTED"},
        {"title": "BOOK_3", "status": "DISCONTINUED"},
    ]
    query = "INSERT INTO books (title, status) VALUES (:title, :status)"
    await database.connect()
    await database.execute_many(query=query, values=test_book_list)
    response = fast_api_test_client.get("/list_books")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "BOOK_1", "status": "AVAILABLE", "renter_id": None},
        {"id": 2, "title": "BOOK_2", "status": "RENTED", "renter_id": None},
        {"id": 3, "title": "BOOK_3", "status": "DISCONTINUED", "renter_id": None},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_change_book_status(fast_api_test_client):
    """
    Test status change to rented or discontinued books
    """
    test_book_list = [
        {"title": "BOOK_1", "status": "RENTED", "renter_id": 1},
        {"title": "BOOK_2", "status": "DISCONTINUED", "renter_id": None},
    ]
    query = "INSERT INTO books (title, status, renter_id) VALUES (:title, :status, :renter_id)"
    await database.connect()
    await database.execute_many(query=query, values=test_book_list)
    for i in range(2):
        fast_api_test_client.post(
            "/book_status", data=json.dumps({"id": (i + 1), "status": "AVAILABLE"})
        )
    response = fast_api_test_client.get("/list_books")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "BOOK_1", "status": "AVAILABLE", "renter_id": None},
        {"id": 2, "title": "BOOK_2", "status": "AVAILABLE", "renter_id": None},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_client_booking_failure(fast_api_test_client):
    """
    Test failure to rent a book given the client is not active
    """
    query = "INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', 0)"
    await database.connect()
    await database.execute(query=query)
    response = fast_api_test_client.post(
        "/rent_book", data=json.dumps({"book_id": 1, "client_id": 1})
    )
    await database.disconnect()
    assert response.json().get("detail") == "Renter Client is not active"


@pytest.mark.asyncio
async def test_book_booking_failure(fast_api_test_client):
    """
    Test failure to rent a book given the book is not available
    """
    queries = [
        ("INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', 1)"),
        "INSERT INTO books (title, status) VALUES ('SOME BOOK 42', 'RENTED')",
    ]
    await database.connect()
    for query in queries:
        await database.execute(query=query)
    response = fast_api_test_client.post(
        "/rent_book", data=json.dumps({"book_id": 1, "client_id": 1})
    )
    await database.disconnect()
    assert response.json().get("detail") == "Book not available to be rented"


@pytest.mark.asyncio
async def test_book_renting(fast_api_test_client):
    """
    Test the action of renting a book
    As of result of the operation the renting status is changed
    and the renter id is added
    """
    queries = [
        "INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', 1)",
        "INSERT INTO clients (name, active) VALUES ('MANUEL RODRIGO', 1)",
        "INSERT INTO books (title, status) VALUES ('SOME BOOK 42', 'AVAILABLE')",
    ]
    await database.connect()
    for query in queries:
        await database.execute(query=query)
    fast_api_test_client.post(
        "/rent_book", data=json.dumps({"book_id": 1, "client_id": 2})
    )
    response = fast_api_test_client.get("/list_books")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "SOME BOOK 42", "status": "RENTED", "renter_id": 2},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_book_search(fast_api_test_client):
    """
    Test book search
    """
    queries = [
        "INSERT INTO books (title, status) VALUES ('DELIBERATE', 'AVAILABLE')",
        "INSERT INTO books (title, status) VALUES ('SUBTLETY', 'DISCONTINUED')",
    ]
    await database.connect()
    for query in queries:
        await database.execute(query=query)
    search_by_id = fast_api_test_client.get("/search_book", data=json.dumps({"id": 2}))
    search_by_name = fast_api_test_client.get(
        "/search_book", data=json.dumps({"title": "SUBTLETY"})
    )
    assert search_by_name.status_code == search_by_id.status_code == 200
    assert (
        search_by_name.json()
        == search_by_id.json()
        == [{"id": 2, "title": "SUBTLETY", "status": "DISCONTINUED", "renter_id": None}]
    )
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_books(fast_api_test_client):
    test_book_list = [{"title": "BOOK_1"}, {"title": "BOOK_2"}]
    await database.connect()
    for book in test_book_list:
        fast_api_test_client.post("/add_book", data=json.dumps(book))
    response = fast_api_test_client.get("/list_books")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "BOOK_1", "status": "AVAILABLE", "renter_id": None},
        {"id": 2, "title": "BOOK_2", "status": "AVAILABLE", "renter_id": None},
    ]
    await database.disconnect()
