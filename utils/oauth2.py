from datetime import timedelta, datetime
from typing import Optional


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import  JWTError, jwt
from decouple import config



SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def createAccessToken(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = generate_expire_date(expires_delta)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def generate_expire_date(expire_delta: Optional[timedelta] = None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days = 1)
    return expire


def accessUserToken(token: str=Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            pass

    except JWTError:
        raise creddentialsExcception()

def creddentialsExcception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )