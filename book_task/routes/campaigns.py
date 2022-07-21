from datetime import datetime, timedelta
from typing import Optional

from databases import Database
from fastapi import HTTPException
from starlette import status


async def create_new_campaign(request_info: dict, database: Database):
    name: Optional[str] = request_info.get("name", None)
    slogan: Optional[str] = request_info.get("slogan", None)
    if name is None or slogan is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    insert_query = "INSERT INTO campaigns (name, slogan) VALUES (:name, :slogan)"
    campaign_to_add = {"name": name, "slogan": slogan}
    try:
        return await database.execute(query=insert_query, values=campaign_to_add)
    except Exception as _:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create a new campaign!",
        )


async def join_new_campaign(request_info: dict, database: Database):
    campaign_id: Optional[str] = request_info.get("campaign_id", None)
    client_id: Optional[str] = request_info.get("client_id", None)
    if client_id is None or campaign_id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    client = await database.fetch_one(
        query=f"SELECT * FROM clients WHERE (id = {client_id} AND active = 1)"
    )
    if client is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client is not active or does not exist!",
        )

    campaign = await database.fetch_one(
        query=f"SELECT * FROM campaigns WHERE id = {campaign_id}"
    )

    if campaign is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client is not active or does not exist!",
        )
    created_date = datetime.strptime(client.created, "%Y-%m-%d %H:%M:%f")
    less_than_hour = created_date < datetime.today() - timedelta(hours=1)
    new_client = 1 if less_than_hour else 0
    insert_query = "INSERT INTO campaign_logs (new_client, client_id, campaign_id) VALUES (:new_client, :client_id, :campaign_id)"
    log_to_create = {
        "new_client": new_client,
        "client_id": client_id,
        "campaign_id": campaign_id,
    }
    try:
        return await database.execute(query=insert_query, values=log_to_create)
    except Exception as _:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create campaign log entry!",
        )
