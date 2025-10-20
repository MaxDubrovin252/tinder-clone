from typing import Annotated
from typing import TYPE_CHECKING
from fastapi import Depends
from core.models import db_helper

if TYPE_CHECKING:
    from core.models import User
    from sqlalchemy.ext.asyncio import AsyncSession


def get_users(
    session: Annotated["AsyncSession", Depends(db_helper.session_dependency)],
):
    yield User.get_db(session)
