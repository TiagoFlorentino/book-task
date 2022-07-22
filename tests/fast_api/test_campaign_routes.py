import json

import pytest

from main import database


@pytest.mark.asyncio
async def test_get_campaigns(fast_api_test_client):
    """
    Test the list operation for campaigns
    """
    test_campaign_list = [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]
    query = "INSERT INTO campaigns (name, slogan, partner_id) VALUES (:name, :slogan, :partner_id)"
    await database.connect()
    await database.execute(
        query="INSERT INTO partners (name, email, active) VALUES ('Mahna', 'mahna_mahna@abc.com', 1)",
    )
    await database.execute_many(query=query, values=test_campaign_list)
    response = fast_api_test_client.get("/list_campaigns")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_campaign(fast_api_test_client):
    """
    Test operation to add campaign to the database
    """
    test_campaign_list = [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]
    await database.connect()
    await database.execute(
        query="INSERT INTO partners (name, email, active) VALUES ('Mahna', 'mahna_mahna@abc.com', 1)",
    )
    for campaign in test_campaign_list:
        fast_api_test_client.post("/add_campaign", data=json.dumps(campaign))

    response = fast_api_test_client.get("/list_campaigns")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_join_campaign(fast_api_test_client):
    """
    Test operation to join a new campaign
    """
    await database.connect()
    await database.execute(
        query="INSERT INTO partners (name, email, active) VALUES ('Mahna', 'mahna_mahna@abc.com', 1)",
    )
    await database.execute(
        query="INSERT INTO campaigns (name, slogan, partner_id) VALUES (:name, :slogan, :partner_id)",
        values={"name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
    )
    await database.execute(
        query="INSERT INTO clients (name, active) VALUES (:name, :active)",
        values={"name": "ANDRE JOSE", "active": 1},
    )
    fast_api_test_client.post(
        "/join_campaign", data=json.dumps({"client_id": 1, "campaign_id": 1})
    )
    response = fast_api_test_client.get("/list_campaign_logs")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "new_client": 1, "campaign_id": 1, "client_id": 1}
    ]
    await database.disconnect()
