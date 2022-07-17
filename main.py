from typing import Optional

from databases import Database
from fastapi import FastAPI, HTTPException
import os

from pydantic import BaseModel
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


@app.get("/clients")
async def clients():
    clients = await database.fetch_all(query="SELECT * FROM clients")
    return clients


@app.post("/add_client/")
async def add_clients(info: Request):
    request_info = await info.json()
    name: Optional[str] = request_info.get("name", None)
    if name is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    insert_query = "INSERT INTO clients (name, active) VALUES (:name, :active)"
    client_to_create = {"name": name, "active": "TRUE"}
    try:
        await database.execute(query=insert_query, values=client_to_create)
    except Exception as _:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
