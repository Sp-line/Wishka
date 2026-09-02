from abc import ABC
from abc import abstractmethod
from uuid import uuid4

from app.schemas.storage import KeyBuild


class S3KeyStrategy[TKeyBuild: KeyBuild](ABC):
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    @abstractmethod
    def generate(self, data: TKeyBuild) -> str: ...


class UserAvatarKeyStrategy(S3KeyStrategy[KeyBuild]):
    def __init__(self) -> None:
        super().__init__(prefix="users/avatars")

    def generate(self, _data: KeyBuild) -> str:
        return f"{self._prefix}/{uuid4()}"


class GiftImageKeyStrategy(S3KeyStrategy[KeyBuild]):
    def __init__(self) -> None:
        super().__init__(prefix="gifts/images")

    def generate(self, _data: KeyBuild) -> str:
        return f"{self._prefix}/{uuid4()}"
