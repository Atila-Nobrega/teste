from fastapi import FastAPI
from routes.v1 import app_v1
from utils.db_object import db

app = FastAPI(title="UFCSmartCampus", description="API da SmartCampus", version="1.0.0")

app.include_router(app_v1, prefix="/v1")

@app.on_event("startup")
async def connect_db():
    await db.connect()

@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()
