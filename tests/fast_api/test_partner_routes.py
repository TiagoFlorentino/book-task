import json

import pytest
from main import database


@pytest.mark.asyncio
async def test_get_partners(
    fast_api_test_client, input_get_partner_list, output_get_partner_list
):
    """
    Test list operation to get partners
    """
    query = "INSERT INTO partners (name, email, active) VALUES (:name, :email, :active)"
    await database.connect()
    await database.execute_many(query=query, values=input_get_partner_list)
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
    assert actual_value == output_get_partner_list
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_and_status_partner(
    fast_api_test_client,
    input_get_partner_list,
    output_get_partner_list,
    output_get_partner_log_list,
):
    """
    Test operation to add and status changes to partners to the database
    """
    await database.connect()
    for partner in input_get_partner_list:
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
    assert actual_value == output_get_partner_list

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
    assert log_value == output_get_partner_log_list
    await database.disconnect()
