from typing import Any

from fastapi_users.models import ID
from fastapi_users.models import OAP
from fastapi_users.models import UP
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.exc import IntegrityError

from app.repositories.handlers.oauth_account import oauth_account_error_handler
from app.repositories.handlers.user import user_error_handler


class ErrorHandlingUserDatabase(SQLAlchemyUserDatabase[UP, ID]):
    async def create(self, create_dict: dict[str, Any]) -> UP:
        try:
            return await super().create(create_dict)
        except IntegrityError as e:
            user_error_handler.handle(e)
            raise

    async def update(self, user: UP, update_dict: dict[str, Any]) -> UP:
        try:
            return await super().update(user, update_dict)
        except IntegrityError as e:
            user_error_handler.handle(e)
            raise

    async def delete(self, user: UP) -> None:
        try:
            return await super().delete(user)
        except IntegrityError as e:
            user_error_handler.handle(e)
            raise

    async def add_oauth_account(self, user: UP, create_dict: dict[str, Any]) -> UP:
        try:
            return await super().add_oauth_account(user, create_dict)
        except IntegrityError as e:
            oauth_account_error_handler.handle(e)
            raise

    async def update_oauth_account(
        self,
        user: UP,
        oauth_account: OAP,
        update_dict: dict[str, Any],
    ) -> UP:
        try:
            return await super().update_oauth_account(user, oauth_account, update_dict)
        except IntegrityError as e:
            oauth_account_error_handler.handle(e)
            raise
