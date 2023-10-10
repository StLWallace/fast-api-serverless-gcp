from fastapi.routing import APIRouter
from models.beers import Beer
from libs.firestore import create_doc, get_doc
from google.cloud.firestore import CollectionReference


class BeerRouter:
    """Class to define routes in /breweries/"""

    def __init__(self, collection_ref: CollectionReference) -> None:
        self.collection_ref = collection_ref

    @property
    def router(self) -> APIRouter:
        router = APIRouter()

        @router.post("/", status_code=200)
        async def create_beer(data: Beer) -> Beer:
            """Create a new beer document"""
            write_result = create_doc(
                collection_ref=self.collection_ref, data=data.model_dump()
            )

            return data

        @router.put("/{beer_id}", status_code=200)
        async def replace_beer(data: Beer, beer_id: str) -> Beer:
            """Replaces a beer document"""
            write_result = create_doc(
                collection_ref=self.collection_ref,
                data=data.model_dump(),
                doc_id=beer_id,
            )

            return data

        @router.get("/{beer_id}", status_code=200)
        async def get_beer(beer_id: str) -> Beer:
            """Gets a beer based on the ID
            Args:  
                beer_id - the doc ID for the beer

            Returns:  
                A doc for the ID
            """
            doc = get_doc(collection_ref=self.collection_ref, doc_id=beer_id)

            return Beer(**doc)

        return router
