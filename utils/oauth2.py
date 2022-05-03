from datetime import timedelta, datetime
from typing import List, Optional
from cv2 import Algorithm
from discord import option

from fastapi import Depends, HTTPException, Status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from decouple import config



SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def createAccessToken(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = generate_expire_date(expires_delta)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def generate_expire_date(expire_delta: Optional[timedelta] = None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days = 1)