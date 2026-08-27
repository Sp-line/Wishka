from typing import Annotated

from annotated_types import Ge
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt


class Id(BaseModel):
    id: PositiveInt

    model_config = ConfigDict(from_attributes=True)


class Pagination(BaseModel):
    skip: Annotated[int, Ge(0)] = 0
    limit: PositiveInt = 100
