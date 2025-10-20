from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
    )
from core.types.user_id import userId
from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped,relationship
if TYPE_CHECKING:   
    from sqlalchemy.ext.asyncio import AsyncSession
    from .profile import Profile
class User(Base,SQLAlchemyBaseUserTable[userId]):
    @classmethod
    def get_db(cls,session:"AsyncSession"):
        return SQLAlchemyUserDatabase(session,cls)
    
    profile: Mapped["Profile"] = relationship("Profile", uselist=False, back_populates="user")

