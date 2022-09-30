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