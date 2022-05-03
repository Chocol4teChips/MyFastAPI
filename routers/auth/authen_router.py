from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm.session import Session
from models.database import get_db
from models.users.users_model import dbUser

from utils.hash import Hash
from utils.oauth2 import createAccessToken

router = APIRouter(
    tags=["authenication"]
)


@router.post("/token")
def login(req: OAuth2PasswordRequestForm = Depends(),
            db: Session = Depends(get_db)):
    user = db.query(dbUser).filter(dbUser.username == req.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    elif not Hash.verify(user.password, req.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )
    else:
        access_token = createAccessToken(data={"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }