import pytest
from main import database


@pytest.mark.asyncio
async def test_get_books(fast_api_test_client):
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
