from typing import Union, List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import *


app = FastAPI()

# create a list of items
db: List[User] = [
    User(
    id = UUID("040d5d7d-6d50-4192-9e90-11ae5de6d906"), 
    first_name="Jamilla", 
    last_name="Ahmed",
    gender=Gender.male,
    roles=[Role.student]
    ), 
    User(
    id = UUID("9b8c33bf-4e1f-41e8-821a-8700e8a5cddf"), 
    first_name="Alex", 
    last_name="Jones",
    gender=Gender.female,
    roles=[Role.admin, Role.user]
    ), 
]

# Index path and return a json
@app.get("/")
def read_root():
    return {"Hello": "World"}


#get all items
@app.get('/api/v1/users')
async def fetch_users():
    return db

# get one item
@app.get('/api/v1/users/{user_id}')
async def fetch_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f'User not with the {user_id} does not found'
    )

# Update an item
@app.put('/api/v1/users')
def update_user(user: UserUpdate):
    for user_found in db:
        if user.id == user_found.id:
            update_user: User = user_found
            db.remove(user_found)
            db.append(update_user)
            return {"Success": "user updated"}
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user.id} faild to update'
    )

#post an item
@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

# delete an item
@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"Succes": "user deleted"}
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user_id} does not exists'
        )