from decimal import Decimal


class GiftLimits:
    PRIORITY_MIN: int = 1
    PRIORITY_MAX: int = 10

    TITLE_MIN: int = 2
    TITLE_MAX: int = 30

    QUANTITY_MIN: int = 1
    QUANTITY_DEFAULT: int = 1

    PRICE_MIN: Decimal = Decimal("0.00")
    PRICE_DEFAULT: Decimal | None = None

    URL_MIN: int = 11
    URL_MAX: int = 2048

    IMAGE_URL_MIN: int = 11
    IMAGE_URL_MAX: int = 2048
