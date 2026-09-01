from app.constants.role import Role
from app.domain.base import EnsureHasRole


class EnsureCanUpdateWishlist(EnsureHasRole):
    @property
    def allowed_roles(self) -> set[Role]:
        return {Role.OWNER}
