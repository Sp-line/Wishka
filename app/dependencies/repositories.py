from dishka import Provider
from dishka import Scope
from dishka import provide

from app.repositories.gift import GiftRepository
from app.repositories.reservation import ReservationRepository
from app.repositories.unit_of_work import UnitOfWork
from app.repositories.user import UserRepository
from app.repositories.wishlist import WishlistRepository
from app.repositories.wishlist_member import WishlistMemberRepository


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_uow = provide(UnitOfWork)

    get_user_repo = provide(UserRepository)

    get_gift_repo = provide(GiftRepository)

    get_wishlist_member_repo = provide(WishlistMemberRepository)

    get_wishlist_repo = provide(WishlistRepository)

    get_reservation_repo = provide(ReservationRepository)
