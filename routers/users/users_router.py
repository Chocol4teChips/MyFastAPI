from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model  import userBase, UserDisplayBase

from models.users.users_model import userBase
from routers.users import users_controller

router = APIRouter(prefix="/users", tags=["users"])




# @router.get("/")
# def get_all_user():
#     return fake_user_db



@router.post("/")
def register_user(req: userBase, db:Session = Depends(get_db)):
    return users_controller.create(db, req)
