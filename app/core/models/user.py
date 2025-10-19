from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
    )
from core.types.user_id import userId
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:   
    from sqlalchemy.ext.asyncio import AsyncSession
    
class User(Base,SQLAlchemyBaseUserTable[userId]):
    
    
    @classmethod
    def get_db(cls,session:"AsyncSession"):
        return SQLAlchemyUserDatabase(session,cls)

