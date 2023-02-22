from typing import Union, List
from uuid import uuid4, UUID
from fastapi import FastAPI
from models import *


app = FastAPI()

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

@app.get("/")
def read_root():
    return {"Hello": "World"}

# get one item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#get all items
@app.get('/api/v1/users')
async def fetch_users():
    return db

#post an item
@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}