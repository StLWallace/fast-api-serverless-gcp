from lib2to3.pytree import Base
from pydantic import BaseModel
from libs.models import Location, ContactInfo


class Brewery(BaseModel):
    """Dataclass for creating or replacing a Brewery record"""

    name: str
    location: Location
    contact: ContactInfo
