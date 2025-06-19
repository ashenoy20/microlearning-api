from fastapi import APIRouter
from app.db.database import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def create_user():
    users = await User.find().to_list()
    return users