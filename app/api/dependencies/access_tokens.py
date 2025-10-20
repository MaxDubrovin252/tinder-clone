from typing import Annotated
from typing import TYPE_CHECKING
from fastapi import Depends
from core.models import db_helper

if TYPE_CHECKING:
    from core.models import AccessToken
    from sqlalchemy.ext.asyncio import AsyncSession


def get_access_tokens(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_dependency),
    ],
):
    yield AccessToken.get_db(session)
