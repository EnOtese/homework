from fastapi import FastAPI
from app1.routers import task, user

app = FastAPI()


# python -m uvicorn app1.main:app1

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
