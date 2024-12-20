from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# http://127.0.0.1:8000/docs
# uvicorn module16_3:app --reload


users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def post_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(new_user_id: int, new_username: str, new_age: int):
    for user in users:
        if user.id == new_user_id:
            user.username = new_username
            user.age = new_age
            return user
    return HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return HTTPException(status_code=404, detail='User was not found')
