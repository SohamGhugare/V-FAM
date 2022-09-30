from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPBearer
from sqlmodel import Session
import jwt

from database import Database
from models import User
from token_verifier import VerifyToken

token_auth_scheme = HTTPBearer()


router = APIRouter()
db = Database()

@router.get("/@me")
async def get_self(response: Response, token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result

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
