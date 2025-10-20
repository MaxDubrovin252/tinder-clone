from typing import Optional


from fastapi_users.db import BaseUserManager
from fastapi_users import IntegerIDMixin
from typing import TYPE_CHECKING
from core.models import User
from core.types.user_id import userIdType
from core.config import settings
import logging

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, userIdType]):
    reset_password_token_secret = settings.access_token.reset_password_key
    verification_token_secret = settings.access_token.verification_key

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning(f"User %r has registered.", user.id)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r", user.id, token
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r", user.id, token
        )
