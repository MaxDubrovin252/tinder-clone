from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase, SQLAlchemyBaseAccessTokenTable
from .base import Base
from core.types.user_id import userId
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class AccessToken(Base,SQLAlchemyBaseAccessTokenTable[userId]):
    user_id:Mapped[userId] = mapped_column(
        Integer,
        ForeignKey("users.id",ondelete="cascade"),
        nullable=False
    ) 
    
    @classmethod
    def get_db(cls,session:"AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session,cls)
    
    
