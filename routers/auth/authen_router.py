from fastapi import APIRouter, Depends, status, HTTPException


router = APIRouter(
    tags=["authenication"]
)


@router.post("/token")
def login():
    return {"hello":"token"}