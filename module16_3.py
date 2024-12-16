from fastapi import FastAPI


app = FastAPI()

# http://127.0.0.1:8000/docs
# uvicorn module16_3:app --reload


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int):
    new_id = int(max(users.keys())) + 1
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    del users[user_id]
    return f'User  {user_id} is deleted'
