from fastapi import HTTPException, status
from pydoc import describe
from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.users.users_model  import userBase, dbUser
from utils.hash import Hash


def create(db: Session, req: userBase):
    new_user = dbUser(
        username = req.username,
        password = Hash.bcrypt(req.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_users(db: Session):
    return db.query(dbUser).all()


def read_user_by_id(db: Session, id: int):
    return db.query(dbUser).filter(dbUser.id == id).first()


def delete(db:Session, id: int):
    user = db.query(dbUser).filter(dbUser.id == id).first()
    db.delete(user)
    db.commit()
    return JSONResponse(content={'details': f"inventory id {id} deleted"})


def update(db:Session, id: int, req: userBase):
    user = db.query(dbUser).filter(dbUser.id == id)
    if user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")
    else:
        user.update(
            {
            dbUser.username: req.username,
            dbUser.password: Hash.bcrypt(req.password)
            }
        )
        db.commit()
        return JSONResponse(
            content={'details':f"user {id} updated successfully"},
            status_code=status.HTTP_200_OK
        )
