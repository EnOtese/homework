from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app4.backend.db_depends import get_db
from typing import Annotated, List
from app4.models import User
from app4.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from app4.models import *
from sqlalchemy import insert
from app4.schemas import CreateUser


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail='User was not found')


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                          firstname=create_user.firstname,
                                          lastname=create_user.lastname,
                                          age=create_user.age,
                                          slug=slugify(create_user.username)))
    db.commit()
    return {'status code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(update(User).values(
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(user_id == User.id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    else:
        db.execute(delete(User))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}

@router.get('/{user_id}/tasks', response_model=List[Task])
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user = await user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = await tasks_by_user_id(db, user_id)
    return tasks