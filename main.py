from databases import Database
from fastapi import FastAPI
import os

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
