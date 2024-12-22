from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

# http://127.0.0.1:8000/docs
# uvicorn module16_5:app --reload

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get("/", response_class=HTMLResponse)
def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int):
    return templates.TemplateResponse("users.html", {"request": request, "user": user_id})


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
