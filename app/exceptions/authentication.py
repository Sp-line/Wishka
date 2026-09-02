class AuthenticationError(Exception):
    pass


class TokenExpiredError(AuthenticationError):
    pass


class TokenInvalidError(AuthenticationError):
    pass
