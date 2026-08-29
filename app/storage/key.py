from abc import ABC
from abc import abstractmethod

from app.schemas.storage import KeyBuild


class S3KeyStrategy[TKeyBuild: KeyBuild](ABC):
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    @abstractmethod
    def generate(self, data: TKeyBuild) -> str: ...
