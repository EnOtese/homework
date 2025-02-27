from fastapi import FastAPI
from app3.routers import user
from app3.routers import task

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)


# python -m uvicorn app2.main:app

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}
