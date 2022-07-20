import json

import pytest

from main import database


@pytest.mark.asyncio
async def test_get_campaigns(fast_api_test_client):
    """
    Test the list operation for campaigns
    """
    test_campaign_list = [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    query = "INSERT INTO campaigns (name, slogan) VALUES (:name, :slogan)"
    await database.connect()
    await database.execute_many(query=query, values=test_campaign_list)
    response = fast_api_test_client.get("/list_campaigns")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    await database.disconnect()


@pytest.mark.asyncio
async def test_add_campaign(fast_api_test_client):
    """
    Test operation to add campaign to the database
    """
    test_campaign_list = [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    await database.connect()
    for campaign in test_campaign_list:
        fast_api_test_client.post("/add_campaign", data=json.dumps(campaign))

    response = fast_api_test_client.get("/list_campaigns")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    await database.disconnect()
