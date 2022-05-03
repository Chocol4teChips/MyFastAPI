from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model  import userBase, UserDisplayBase

from models.users.users_model import userBase
from routers.users import users_controller

from utils.oauth2 import accessUserToken

router = APIRouter(prefix="/users", tags=["users"])



@router.get("/",  response_model=List[UserDisplayBase], dependencies=[Depends(accessUserToken)])
def get_all_users(db:Session = Depends(get_db)):
    return users_controller.read_users(db)


@router.post("/")
def register_user(req: userBase, db:Session = Depends(get_db)):
    return users_controller.create(db, req)


@router.get("/{id}", response_model=UserDisplayBase, dependencies=[Depends(accessUserToken)])
def userByID(id: int, db: Session = Depends(get_db)):
    return users_controller.read_user_by_id(db, id)


@router.put("/{id}", dependencies=[Depends(accessUserToken)])
def updateUser(id: int, req: userBase, db: Session = Depends(get_db)):
    return users_controller.update(db, id, req)


@router.delete("/{id}", dependencies=[Depends(accessUserToken)])
def deleteApi(id: int, db: Session = Depends(get_db)):
    return users_controller.delete(db, id)