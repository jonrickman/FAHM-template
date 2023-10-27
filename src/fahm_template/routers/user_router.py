from fastapi.encoders import jsonable_encoder
from fastapi import status, Body, APIRouter
from fastapi.responses import Response, JSONResponse
import motor.motor_asyncio
from fahm_template import MONGODB_URL
from fahm_template import User
from typing import List

PREFIX = "/users"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
collection = client.test["user_table"]
router = APIRouter(prefix=PREFIX)


@router.get("/", response_description="Just a hello world", response_model=List[User])
async def list_users():
    print(MONGODB_URL)
    users = await collection.find().to_list(1000)
    return users


@router.post("/", response_description="Add new user", response_model=User)
async def create_user(user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = await collection.insert_one(user)
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
