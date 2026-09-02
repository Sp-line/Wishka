from enum import StrEnum


class WishlistLimits:
    TITLE_MIN: int = 2
    TITLE_MAX: int = 20

    INVITE_TOKEN_MIN: int = 16
    INVITE_TOKEN_MAX: int = 64

    DESCRIPTION_MIN: int = 2
    DESCRIPTION_MAX: int = 500

    PRIVACY_MAX: int = 16


class WishlistPrivacy(StrEnum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    WITH_LINK = "WITH_LINK"
    FRIENDS = "FRIENDS"
