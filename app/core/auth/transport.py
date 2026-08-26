from fastapi_users.authentication import CookieTransport

from app.core.config import settings

cookie_transport = CookieTransport(
    cookie_max_age=settings.auth.lifetime_seconds,
    cookie_secure=settings.auth.cookie_secure,
)
