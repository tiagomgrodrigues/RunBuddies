from fastapi import FastAPI
from databases import Database

DATABASE_URL = "postgresql://runbuddies:supersecret@db:5432/runbuddies_db"

database = Database(DATABASE_URL)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    query = "SELECT 'Hello from RunBuddies 👟' AS message"
    result = await database.fetch_one(query)
    return {"message": result["message"]}