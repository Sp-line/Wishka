from fastapi_users import FastAPIUsers

from app.core.auth.backend import auth_backend
from app.core.models.user import User
from app.core.types.user import UserID
from app.dependencies.auth import get_user_manager

fastapi_users = FastAPIUsers[User, UserID](
    get_user_manager,
    [auth_backend],
)
