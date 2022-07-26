from typing import Optional

from databases import Database
from fastapi import HTTPException
from starlette import status


async def client_search(request_info: dict, database: Database):
    """
    Search client by ID or Name
    """
    name: Optional[str] = request_info.get("name", None)
    id: Optional[int] = request_info.get("id", None)
    if name is None and id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing name or ID parameters",
        )
    if name is not None:
        return await database.fetch_all(
            query="SELECT * FROM clients WHERE name = :name", values={"name": name}
        )
    else:
        return await database.fetch_all(
            query="SELECT * FROM clients WHERE id = :id", values={"id": id}
        )


async def change_client_status(request_info: dict, database: Database):
    """
    Change client status - Active is a bool but stored as an int in the DB
    """
    id: Optional[int] = request_info.get("id", None)
    client_status: Optional[int] = request_info.get("active", None)
    if id is None or client_status is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID and status of the client were not provided",
        )
    # False = 0 // True = 1
    update_status = 1 if client_status else 0
    return await database.execute(
        query="UPDATE clients SET active = :active WHERE id = :id",
        values={"id": id, "active": update_status},
    )


async def create_client(request_info: dict, database: Database):
    """
    Create a new client
    """
    name: Optional[str] = request_info.get("name", None)
    if name is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client Name was not provided",
        )
    insert_query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    client_to_create = {"name": name, "active": 1}
    try:
        return await database.execute(query=insert_query, values=client_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
