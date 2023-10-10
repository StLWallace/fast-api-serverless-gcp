from unicodedata import decimal
from pydantic import BaseModel
from typing import Literal


class Beer(BaseModel):
    """Dataclass for a beer
    The style enum isn't exhaustive so don't @me beer nerds
    """

    name: str
    brewery_id: str
    style: Literal["Ale", "Lager", "Stout", "Porter", "Sour", "Saison", "Barleywine"]
    abv: float
