from typing import Optional

from databases import Database
from fastapi import FastAPI, HTTPException
import os

from starlette import status
from starlette.requests import Request

from book_task.routes.book import search_books, rent_books, change_book_status
from book_task.routes.client import client_search, change_client_status, create_client

app = FastAPI()


current_env = os.environ.get("CURRENT_ENV", "")

if current_env == "test":
    # Test Case only
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
    return await client_search(request_info, database)


@app.post("/client_status")
async def client_status(info: Request):
    request_info = await info.json()
    return await change_client_status(request_info, database)


@app.post("/add_client")
async def add_client(info: Request):
    request_info = await info.json()
    return await create_client(request_info, database)


# BOOK OPERATIONS!
@app.get("/list_books")
async def list_books():
    return await database.fetch_all(query="SELECT * FROM books")


@app.get("/search_book")
async def search_book(info: Request):
    request_info = await info.json()
    return await search_books(request_info, database)


@app.post("/rent_book")
async def rent_book(info: Request):
    request_info = await info.json()
    return await rent_books(request_info, database)


@app.post("/book_status")
async def book_status(info: Request):
    request_info = await info.json()
    return await change_book_status(request_info, database)
