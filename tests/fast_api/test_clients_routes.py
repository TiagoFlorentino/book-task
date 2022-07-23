import json
import pytest
from main import database


@pytest.mark.asyncio
async def test_get_clients(
    fast_api_test_client, input_get_clients_list, output_get_clients_list
):
    """
    Test list operation to get clients
    """
    query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    await database.connect()
    await database.execute_many(query=query, values=input_get_clients_list)
    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    actual_value = []
    for client in response.json():
        actual_value.append(
            {
                "id": client.get("id"),
                "name": client.get("name"),
                "active": client.get("active"),
            }
        )
    assert actual_value == output_get_clients_list
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_clients(fast_api_test_client, output_get_clients_list):
    """
    Test operation to add clients to the database
    """
    test_user_list = [
        {"name": "ANDRE JOSE"},
        {"name": "RITA MARIA"},
    ]
    await database.connect()
    for user in test_user_list:
        fast_api_test_client.post("/add_client", data=json.dumps(user))

    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    actual_value = []
    for client in response.json():
        actual_value.append(
            {
                "id": client.get("id"),
                "name": client.get("name"),
                "active": client.get("active"),
            }
        )
    assert actual_value == output_get_clients_list
    await database.disconnect()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_parameter, input_status, output_status",
    [(True, 0, 1), (False, 1, 0)],
)
async def test_status_management_client(
    fast_api_test_client, request_parameter, input_status, output_status
):
    """
    Test activation or deactivation of the clients
    :param fast_api_test_client: Test Client
    :param input_status: input status of the client on the DB
    :param test_request: endpoint which is used to make the request
    :param output_status: output status of the client to be update on the DB
    """
    query = f"INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', '{request_parameter}')"
    await database.connect()
    await database.execute(query=query)
    fast_api_test_client.post(
        "/client_status", data=json.dumps({"id": 1, "active": output_status})
    )
    response = fast_api_test_client.get("/list_clients")
    assert response.status_code == 200
    actual_value = []
    for client in response.json():
        actual_value.append(
            {
                "id": client.get("id"),
                "name": client.get("name"),
                "active": client.get("active"),
            }
        )
    assert actual_value == [{"id": 1, "name": "ANDRE JOSE", "active": output_status}]
    await database.disconnect()


@pytest.mark.asyncio
async def test_client_search(fast_api_test_client, input_get_clients_list):
    """
    Test client search by name and ID
    """
    query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    await database.connect()
    await database.execute_many(query=query, values=input_get_clients_list)
    response_by_id = fast_api_test_client.get(
        "/search_client", data=json.dumps({"id": 2})
    )
    response_by_name = fast_api_test_client.get(
        "/search_client", data=json.dumps({"name": "RITA MARIA"})
    )
    assert response_by_name.status_code == response_by_id.status_code == 200
    by_name = response_by_name.json()[0]
    by_id = response_by_id.json()[0]
    assert (
        [
            {
                "id": by_name.get("id"),
                "name": by_name.get("name"),
                "active": by_name.get("active"),
            }
        ]
        == [
            {
                "id": by_id.get("id"),
                "name": by_id.get("name"),
                "active": by_id.get("active"),
            }
        ]
        == [{"id": 2, "name": "RITA MARIA", "active": 1}]
    )
    await database.disconnect()
