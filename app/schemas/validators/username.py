from typing import LiteralString

from pydantic_core import PydanticCustomError

from app.constants.user import UserLimits


def validate_username_characters(value: str) -> str:
    invalid_chars = set(value) - UserLimits.ALLOWED_CHARS
    if invalid_chars:
        err_type: LiteralString = "username_invalid_characters"
        err_msg: LiteralString = "Username contains invalid characters: {invalid_chars}. Only lowercase Latin letters, numbers, '.', and '_' are allowed"  # noqa: E501
        raise PydanticCustomError(
            err_type,
            err_msg,
            {"invalid_chars": ", ".join(sorted(invalid_chars))},
        )
    return value


def validate_username_start_finish(value: str) -> str:
    if value.startswith((".", "_")) or value.endswith((".", "_")):
        err_type: LiteralString = "username_invalid_boundary"
        err_msg: LiteralString = "Username cannot start or end with a dot or underscore"
        raise PydanticCustomError(err_type, err_msg)
    return value


def validate_username_consecutive_symbols(value: str) -> str:
    forbidden_sequences = ("..", "__", "._", "_.")
    for seq in forbidden_sequences:
        if seq in value:
            err_type: LiteralString = "username_consecutive_symbols"
            err_msg: LiteralString = "Username cannot contain consecutive special characters like '..', '__', '._', or '_.'"  # noqa: E501
            raise PydanticCustomError(err_type, err_msg)
    return value


def validate_username_not_all_digits(value: str) -> str:
    if value.isdigit():
        err_type: LiteralString = "username_only_digits"
        err_msg: LiteralString = "Username cannot consist entirely of numbers"
        raise PydanticCustomError(err_type, err_msg)
    return value
