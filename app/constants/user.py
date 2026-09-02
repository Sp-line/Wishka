class UserLimits:
    AVATAR_S3_KEY_MIN: int = 20
    AVATAR_S3_KEY_MAX: int = 255

    USERNAME_MIN: int = 2
    USERNAME_MAX: int = 20
    ALLOWED_CHARS: frozenset[str] = frozenset("abcdefghijklmnopqrstuvwxyz0123456789_.")
