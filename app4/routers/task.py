from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app4.backend.db_depends import get_db
from typing import Annotated
from app4.models import Task
from app4.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from app4.routers.user import user_by_id

from app4.models import *
from sqlalchemy import insert
router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(task_id))
    if task is not None:
        return task
    else:
        raise HTTPException(status_code=404, detail='Task was not found')


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = await user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    db.execute(insert(Task).values(title=create_task.title,
                                          content=create_task.content,
                                          priority=create_task.priority,
                                          user_id=user_id,
                                          slug=slugify(create_task.title)))
    db.commit()
    return {'status code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        db.execute(update(Task).values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(task_id == Task.id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    else:
        db.execute(delete(Task))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
