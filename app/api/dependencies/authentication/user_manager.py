from fastapi import Depends
from fastapi_users.manager import UserManager
from .users import get_users


async def get_user_manager(user_db=Depends(get_users)):
    yield UserManager(user_db)
