from fastapi_users.authentication import AuthenticationBackend

from app.core.auth.strategy import get_jwt_strategy
from app.core.auth.transport import cookie_transport

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
