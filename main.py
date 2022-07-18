from typing import Optional

from databases import Database
from fastapi import FastAPI, HTTPException
import os

from starlette import status
from starlette.requests import Request

app = FastAPI()


current_env = os.environ.get("CURRENT_ENV", "")

if current_env == "test":
    database = Database("sqlite:///test_db.db", force_rollback=True)
else:
    database = Database("sqlite:///database.db")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


# CLIENT OPERATIONS!
@app.get("/list_clients")
async def list_clients():
    return await database.fetch_all(query="SELECT * FROM clients")


@app.get("/search_client")
async def search_client(info: Request):
    request_info = await info.json()
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


@app.post("/activate_client")
async def activate_client(info: Request):
    request_info = await info.json()
    id: Optional[int] = request_info.get("id", None)
    if id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID of the client was not provided",
        )
    return await database.execute(
        query="UPDATE clients SET active = 'TRUE' WHERE id = :id", values={"id": id}
    )


@app.post("/deactivate_client")
async def deactivate_client(info: Request):
    request_info = await info.json()
    id: Optional[int] = request_info.get("id", None)
    if id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID of the client was not provided",
        )
    return await database.execute(
        query="UPDATE clients SET active = 'FALSE' WHERE id = :id", values={"id": id}
    )


@app.post("/add_client")
async def add_client(info: Request):
    request_info = await info.json()
    name: Optional[str] = request_info.get("name", None)
    if name is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client Name was not provided",
        )
    insert_query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    client_to_create = {"name": name, "active": "TRUE"}
    try:
        return await database.execute(query=insert_query, values=client_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# BOOK OPERATIONS!
@app.get("/list_books")
async def list_books():
    return await database.fetch_all(query="SELECT * FROM books")


@app.post("/rent_book")
async def rent_book(info: Request):
    request_info = await info.json()
    book_id: Optional[str] = request_info.get("book_id", None)
    client_id: Optional[str] = request_info.get("client_id", None)
    if book_id is None or client_id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    renter_client = await database.fetch_one(
        query=f"SELECT * FROM clients WHERE id = {client_id}"
    )
    if renter_client.active != "TRUE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Renter Client is not active",
        )
    book_to_rend = await database.fetch_one(
        query=f"SELECT * FROM books WHERE id = {book_id}"
    )
    if book_to_rend.status != "AVAILABLE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book not available to be rented",
        )

    return await database.execute(
        query="UPDATE books SET status = 'RENTED', renter_id = :client_id WHERE id = :book_id",
        values={"client_id": client_id, "book_id": book_id},
    )


@app.post("/book_status")
async def book_status(info: Request):
    request_info = await info.json()
    id: Optional[int] = request_info.get("id", None)
    book_status: Optional[int] = request_info.get("status", None)
    if id is None or status is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID or Updated status of the book were not provided",
        )
    if status in ["AVAILABLE", "DISCONTINUED"]:
        return await database.execute(
            query="UPDATE books SET status = :status, renter_id = NULL WHERE id = :id",
            values={"id": id, "status": book_status},
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Failed to process request",
    )
