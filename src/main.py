from typing import List
from fastapi import FastAPI, HTTPException
import uuid
from model.models import User, UserUpdateRequest
from data.dummy_data import dummy_users

app = FastAPI()

db: List[User] = dummy_users


@app.get("/")
async def hello():
    return {"msg": "Hello There!"}


@app.get("/api/v1/users/")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: uuid.UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404, detail={f"User with id: {user_id} does not exits"}
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: uuid.UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"User with id: {user_id} does not exists."
    )