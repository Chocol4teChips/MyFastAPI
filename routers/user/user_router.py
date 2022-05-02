from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


fake_user_db = [{"username": "test1"}, {"password": "testpass"}]


@router.get("/")
def get_all_user():
    return fake_user_db
