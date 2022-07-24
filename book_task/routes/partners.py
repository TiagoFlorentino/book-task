from time import sleep
from typing import Optional

from databases import Database
from fastapi import HTTPException
from starlette import status


async def change_partner_status(request_info: dict, database: Database):
    """
    Change partner status//active or not - status is bool but stored as an int in the DB
    """
    id: Optional[int] = request_info.get("id", None)
    active: Optional[bool] = request_info.get("active", None)
    if id is None or active is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID and status of the client were not provided",
        )
    # False = 0 // True = 1
    update_status = 1 if active else 0
    await database.execute(
        query="UPDATE partners SET active = :active WHERE id = :id",
        values={"id": id, "active": update_status},
    )
    insert_query = "INSERT INTO partner_log (partner_id, active) VALUES (:id, :active)"
    log_to_create = {"id": int(id), "active": update_status}
    try:
        return await database.execute(query=insert_query, values=log_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def add_new_partner(request_info: dict, database: Database):
    """
    Add a new partner which provides name and email
    """
    name: Optional[str] = request_info.get("name", None)
    email: Optional[str] = request_info.get("email", None)
    if name is None or email is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Partner Name or Email was not provided",
        )
    insert_query = (
        "INSERT INTO partners (name, email, active) VALUES (:name, :email, 1)"
    )
    partner_to_create = {"name": name, "email": email}
    try:
        await database.execute(query=insert_query, values=partner_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    partner = await database.fetch_one(
        query=f"SELECT * FROM partners WHERE email = '{email}'"
    )
    insert_query = "INSERT INTO partner_log (partner_id, active) VALUES (:id, :active)"
    log_to_create = {"id": int(partner.id), "active": 1}
    try:
        return await database.execute(query=insert_query, values=log_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
