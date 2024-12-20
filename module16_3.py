from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# http://127.0.0.1:8000/docs
# uvicorn module16_3:app --reload


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description='Enter username, Example: UrbanUser',
                                                  regex="^[a-zA-Z0-9_-]+$")],
                    age: Annotated[int, Path(gt=18, le=100, description='Enter age, Example: 24')]):
    new_id = int(max(users.keys())) + 1
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(gt=1, le=100, description='Enter User ID, Example: 1')],
                      username: Annotated[str, Path(min_length=5, max_length=20,
                                                    description='Enter username, Example: UrbanUser',
                                                    regex="^[a-zA-Z0-9_-]+$")],
                      age: Annotated[int, Path(gt=18, le=100, description='Enter age, Example: 24')]):
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(gt=1, le=100, description='Enter User ID, Example: 1')]):
    del users[user_id]
    return f'User  {user_id} is deleted'
