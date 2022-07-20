import pytest

from main import database


@pytest.mark.asyncio
async def test_get_campaigns(fast_api_test_client):
    """
    Test the list operation for campaigns
    """
    test_book_list = [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    query = "INSERT INTO campaigns (name, slogan) VALUES (:name, :slogan)"
    await database.connect()
    await database.execute_many(query=query, values=test_book_list)
    response = fast_api_test_client.get("/list_campaigns")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A"},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B"},
    ]
    await database.disconnect()
