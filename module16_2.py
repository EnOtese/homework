from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# http://127.0.0.1:8000/docs
# uvicorn module16_2:app --reload

@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def admin_root():
    return "Вы вошли как администратор"


@app.get("/users/{user_id}")
async def user_root(user_id: Annotated[int, Path(gt=0, le=100, description='Enter User ID, Example: 1')]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description='Enter username, Example: UrbanUser',
                                                  regex="^[a-zA-Z0-9_-]+$")],
                    age: Annotated[int, Path(gt=18, le=100, description='Enter age, Example: 24')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
