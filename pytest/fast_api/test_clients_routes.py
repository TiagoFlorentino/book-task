import json

import pytest

from main import database


@pytest.mark.asyncio
async def test_get_clients(fast_api_test_client):
    test_user_list = [
        {"name": "ANDRE JOSE", "active": "TRUE"},
        {"name": "RITA MARIA", "active": "TRUE"},
    ]
    query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    await database.connect()
    await database.execute_many(query=query, values=test_user_list)
    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "ANDRE JOSE", "active": "TRUE"},
        {"id": 2, "name": "RITA MARIA", "active": "TRUE"},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_clients(fast_api_test_client):
    test_user_list = [
        {"name": "ANDRE JOSE"},
        {"name": "RITA MARIA"},
    ]
    await database.connect()
    for user in test_user_list:
        fast_api_test_client.post("/add_client/", data=json.dumps(user))

    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "ANDRE JOSE", "active": "TRUE"},
        {"id": 2, "name": "RITA MARIA", "active": "TRUE"},
    ]
    await database.disconnect()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_status, test_request, output_status",
    [("FALSE", "/activate_client", "TRUE"), ("TRUE", "/deactivate_client", "FALSE")],
)
async def test_status_management_client(
    fast_api_test_client, input_status, test_request, output_status
):
    query = (
        f"INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', '{input_status}')"
    )
    await database.connect()
    await database.execute(query=query)
    fast_api_test_client.post(test_request, data=json.dumps({"id": 1}))
    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "ANDRE JOSE", "active": output_status}]
    await database.disconnect()


@pytest.mark.asyncio
async def test_client_search(fast_api_test_client):
    test_user_list = [
        {"name": "ANDRE JOSE", "active": "TRUE"},
        {"name": "RITA MARIA", "active": "TRUE"},
    ]
    query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    await database.connect()
    await database.execute_many(query=query, values=test_user_list)
    response_by_id = fast_api_test_client.get(
        "/search_client", data=json.dumps({"id": 2})
    )
    response_by_name = fast_api_test_client.get(
        "/search_client", data=json.dumps({"name": "RITA MARIA"})
    )
    assert response_by_name.status_code == response_by_id.status_code == 200
    assert (
        response_by_name.json()
        == response_by_id.json()
        == [{"id": 2, "name": "RITA MARIA", "active": "TRUE"}]
    )
    await database.disconnect()
