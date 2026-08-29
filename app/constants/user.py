class UserLimits:
    PHOTO_URL_MIN: int = 11
    PHOTO_URL_MAX: int = 2048

    USERNAME_MIN: int = 2
    USERNAME_MAX: int = 20
    ALLOWED_CHARS: frozenset[str] = frozenset("abcdefghijklmnopqrstuvwxyz0123456789_.")
