from dishka import Provider
from dishka import Scope
from dishka import provide

from app.domain.wishlist import EnsureCanUpdateWishlist


class DomainProvider(Provider):
    scope = Scope.APP

    get_ensure_can_update_wishlist = provide(EnsureCanUpdateWishlist)
