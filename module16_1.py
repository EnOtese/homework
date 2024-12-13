from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:8000/docs
# uvicorn module16_1:app --reload

@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def admin_root():
    return "Вы вошли как администратор"


@app.get("/users/{user_id}")
async def user_root(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/users/")
async def user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
