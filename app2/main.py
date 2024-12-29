from fastapi import FastAPI
from app2.routers import task, user

app = FastAPI()


# python -m uvicorn app2.main:app

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
