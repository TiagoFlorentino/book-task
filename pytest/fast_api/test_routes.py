import pytest

from main import database


@pytest.mark.asyncio
async def test_request_example(fast_api_test_client):
    test_user_list = [
        {"name": "ANDRE JOSE", "active": "TRUE"},
        {"name": "RITA MARIA", "active": "TRUE"},
    ]
    query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    await database.connect()
    await database.execute_many(query=query, values=test_user_list)
    response = fast_api_test_client.get("/clients")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "ANDRE JOSE", "active": "TRUE"},
        {"id": 2, "name": "RITA MARIA", "active": "TRUE"},
    ]
    await database.disconnect()
