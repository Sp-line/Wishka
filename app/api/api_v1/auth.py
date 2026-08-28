from fastapi import APIRouter

from app.core.auth.backend import auth_backend
from app.core.auth.clients import google_oauth_client
from app.core.auth.fastapi_users import fastapi_users
from app.core.config import settings
from app.schemas.user import UserCreate
from app.schemas.user import UserRead

router = APIRouter(prefix=settings.api.v1.auth)

router.include_router(fastapi_users.get_auth_router(auth_backend))

router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

router.include_router(fastapi_users.get_verify_router(UserRead))

router.include_router(fastapi_users.get_reset_password_router())

router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        auth_backend,
        settings.auth.secret.get_secret_value(),
        str(settings.oauth.google.redirect_url),
        associate_by_email=settings.oauth.google.associate_by_email,
        is_verified_by_default=settings.oauth.google.is_verified_by_default,
        csrf_token_cookie_secure=settings.auth.cookie_secure,
    ),
    prefix="/google",
)
