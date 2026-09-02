from enum import StrEnum


class AuthenticationErrorMessage(StrEnum):
    TOKEN_EXPIRED = "Token has expired."  # noqa: S105
    TOKEN_INVALID = "Token is invalid or corrupted."  # noqa: S105
