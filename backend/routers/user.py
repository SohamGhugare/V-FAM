from fastapi import APIRouter, Depends
from database import Database
from models import User
from sqlmodel import Session

router = APIRouter()
db = Database()

@router.get("/@me")
async def get_self():
    return

@router.post("/create-user")
async def create_user(*, session: Session = Depends(db.get_session), user: User):
    db.create_user(User.from_orm(user))
    return {"data": "User created"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db.delete_user(user_id)
    return {"data": "User deleted"}

@router.get("/@{username}")
async def get_user(username: str):
    user = db.get_user_by_name(username)
    return {"data": user}
    