from typing import Optional
from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    """Common model for location"""

    city: str
    state: str
    zipcode: str


class ContactInfo(BaseModel):
    """Data class for contact info"""

    phone_number: Optional[str] = None
    email: Optional[str] = None
