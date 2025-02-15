from fastapi import APIRouter, HTTPException
from app.models import User
from app.crud import create_user, get_users
from app.database import users_container

router = APIRouter()

@router.post("/", response_model=User)
def add_user(user: User):
    try:
        return create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")

@router.get("/", response_model=list[User])
def get_user_list():
    return get_users()

