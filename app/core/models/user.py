from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin
from app.core.types.user import UserID


class User(Base, IntIdPkMixin, ObservableMixin, SQLAlchemyBaseUserTable[UserID]):
    pass
