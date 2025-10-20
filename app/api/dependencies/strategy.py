from fastapi import Depends
from core.models import db_helper
from typing import Annotated
from typing import TYPE_CHECKING
from core.config import settings

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users_db_sqlalchemy.access_token import AccessTokenDatabase
    from fastapi_users_db_sqlalchemy.generics import DatabaseStrategy


def get_db_stategy(
    access_token_db: Annotated["AccessTokenDatabase[AccessToken]", Depends(...)],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
