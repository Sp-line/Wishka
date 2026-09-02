from datetime import UTC
from datetime import datetime
from datetime import timedelta

import jwt
from pydantic import SecretStr
from pydantic import ValidationError

from app.constants.auth import JWTAlgorithm  # noqa: TC001
from app.exceptions.authentication import TokenExpiredError
from app.exceptions.authentication import TokenInvalidError
from app.schemas.token import JWTPayloadBase


class JWTService:
    def __init__(
        self,
        secret: SecretStr,
        algorithm: JWTAlgorithm,
    ) -> None:
        self.secret = secret
        self.algorithm = algorithm

    def create_token(self, payload: JWTPayloadBase, lifetime_seconds: int) -> str:
        payload.exp = datetime.now(UTC) + timedelta(seconds=lifetime_seconds)
        return jwt.encode(
            payload=payload.model_dump(),
            key=self.secret.get_secret_value(),
            algorithm=self.algorithm,
        )

    def verify_token[TJWTPayload: JWTPayloadBase](
        self,
        token: str,
        schema: type[TJWTPayload],
    ) -> TJWTPayload:
        try:
            decoded_data = jwt.decode(
                jwt=token,
                key=self.secret.get_secret_value(),
                algorithms=[self.algorithm],
            )
            return schema.model_validate(decoded_data)

        except jwt.ExpiredSignatureError:
            raise TokenExpiredError from None
        except jwt.InvalidTokenError, ValidationError:
            raise TokenInvalidError from None
