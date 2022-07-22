import json

import pytest
from main import database


@pytest.mark.asyncio
async def test_get_partners(fast_api_test_client):
    """
    Test list operation to get partners
    """
    test_partern_list = [
        {"name": "Mahna Mahna", "email": "mahna_mahna@xyz.com", "active": 1},
        {"name": "Bippadotta", "email": "bippadotta@xyz.com", "active": 1},
    ]
    query = "INSERT INTO partners (name, email, active) VALUES (:name, :email, :active)"
    await database.connect()
    await database.execute_many(query=query, values=test_partern_list)
    response = fast_api_test_client.get("/list_partners")
    assert response.status_code == 200
    actual_value = []
    for partner in response.json():
        actual_value.append(
            {
                "id": partner.get("id"),
                "name": partner.get("name"),
                "email": partner.get("email"),
                "active": partner.get("active"),
            }
        )
    assert actual_value == [
        {"id": 1, "name": "Mahna Mahna", "email": "mahna_mahna@xyz.com", "active": 1},
        {"id": 2, "name": "Bippadotta", "email": "bippadotta@xyz.com", "active": 1},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_and_status_partner(fast_api_test_client):
    """
    Test operation to add and status changes to partners to the database
    """
    test_partern_list = [
        {"name": "Mahna Mahna", "email": "mahna_mahna.xyz.com"},
        {"name": "Bippadotta", "email": "bippadotta.xyz.com"},
    ]
    await database.connect()
    for partner in test_partern_list:
        fast_api_test_client.post("/add_partner", data=json.dumps(partner))
    response = fast_api_test_client.get("/list_partners")
    assert response.status_code == 200
    actual_value = []
    for partner in response.json():
        actual_value.append(
            {
                "id": partner.get("id"),
                "name": partner.get("name"),
                "email": partner.get("email"),
                "active": partner.get("active"),
            }
        )
    assert actual_value == [
        {"id": 1, "name": "Mahna Mahna", "email": "mahna_mahna.xyz.com", "active": 1},
        {"id": 2, "name": "Bippadotta", "email": "bippadotta.xyz.com", "active": 1},
    ]

    fast_api_test_client.post(
        "/partner_status", data=json.dumps({"id": 1, "active": False})
    )
    log_response = fast_api_test_client.get("/list_partner_logs")
    log_value = []
    for log_local in log_response.json():
        log_value.append(
            {
                "id": log_local.get("id"),
                "partner_id": log_local.get("partner_id"),
                "active": log_local.get("active"),
            }
        )
    assert log_value == [
        {"id": 1, "partner_id": 1, "active": 1},
        {"id": 2, "partner_id": 2, "active": 1},
        {"id": 3, "partner_id": 1, "active": 0},
    ]
    await database.disconnect()
