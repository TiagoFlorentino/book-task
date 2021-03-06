from typing import Optional

from databases import Database
from fastapi import HTTPException
from starlette import status


async def search_books(request_info: dict, database: Database):
    """
    Search a book by it's name or ID
    """
    title: Optional[str] = request_info.get("title", None)
    id: Optional[int] = request_info.get("id", None)
    if title is None and id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing name or ID parameters",
        )
    if title is not None:
        return await database.fetch_all(
            query="SELECT * FROM books WHERE title = :title", values={"title": title}
        )
    else:
        return await database.fetch_all(
            query="SELECT * FROM books WHERE id = :id", values={"id": id}
        )


async def rent_books(request_info: dict, database: Database):
    """
    Rent a book using book_id and client_id
    """
    book_id: Optional[str] = request_info.get("book_id", None)
    client_id: Optional[str] = request_info.get("client_id", None)
    if book_id is None or client_id is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing required parameters",
        )
    renter_client = await database.fetch_one(
        query=f"SELECT * FROM clients WHERE (id = {client_id} AND active = 1)"
    )
    if renter_client is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Renter Client is not active",
        )
    book_to_rent = await database.fetch_one(
        query=f"SELECT * FROM books WHERE (id = {book_id} AND status = 'AVAILABLE')"
    )
    if book_to_rent is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book not available to be rented",
        )

    query_variable = {"client_id": client_id, "book_id": book_id}
    try:
        # Add renting log
        await database.execute(
            query="INSERT INTO renting_log (book_id, client_id) VALUES (:book_id, :client_id)",
            values=query_variable,
        )
        # Change book status
        return await database.execute(
            query="UPDATE books SET status = 'RENTED', renter_id = :client_id WHERE id = :book_id",
            values=query_variable,
        )
    except Exception as _:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to store the new book!",
        )


async def change_book_status(request_info: dict, database: Database):
    """
    Change the status of the book by AVAILABLE or DISCONTINUED
    """
    id: Optional[int] = request_info.get("id", None)
    book_status: Optional[int] = request_info.get("status", None)
    if id is None or status is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID or Updated status of the book were not provided",
        )
    if book_status not in ["AVAILABLE", "DISCONTINUED"]:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Status not AVAILABLE or DISCONTINUED!",
        )
    # Change book status
    return await database.execute(
        query="UPDATE books SET status = :status, renter_id = NULL WHERE id = :id",
        values={"id": id, "status": book_status},
    )


async def create_book(request_info: dict, database: Database):
    """
    Add a new book to the library
    """
    title: Optional[str] = request_info.get("title", None)
    if title is None:
        # The server will not process the following request due to the missing field
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client Name was not provided",
        )
    insert_query = "INSERT INTO books (title, status) VALUES (:title, :status)"
    book_to_create = {"title": title, "status": "AVAILABLE"}
    try:
        return await database.execute(query=insert_query, values=book_to_create)
    except Exception as _:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to store the new book!",
        )
