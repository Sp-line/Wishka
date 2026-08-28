from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import FastAPI

from app.exceptions.handlers.db import register_db_exception_handlers


def register_exception_handlers(app: FastAPI) -> None:
    register_db_exception_handlers(app)
