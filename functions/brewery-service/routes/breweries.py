from fastapi.routing import APIRouter
from models.breweries import Brewery


brewery_router = APIRouter()


@brewery_router.post("/")
async def create_brewery(data: Brewery) -> Brewery:
    """Creates a new Brewery record
    
    """
    return data
