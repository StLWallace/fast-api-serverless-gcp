from fastapi.routing import APIRouter
from models.breweries import Brewery
from libs.firestore import create_doc, get_doc
from google.cloud.firestore import CollectionReference


class BreweryRouter:
    """Class to define routes in /breweries/"""

    def __init__(self, collection_ref: CollectionReference) -> None:
        self.collection_ref = collection_ref

    @property
    def router(self) -> APIRouter:
        router = APIRouter()

        @router.post("/", status_code=200)
        async def create_brewery(data: Brewery) -> Brewery:
            """Creates a new Brewery record
            
            """
            write_result = create_doc(
                collection_ref=self.collection_ref, data=data.model_dump()
            )
            print(write_result)

            return data

        @router.put("/{brewery_id}", status_code=200)
        async def replace_brewery(data: Brewery, brewery_id: str) -> Brewery:
            """Replaces a new Brewery record
            
            """
            write_result = create_doc(
                collection_ref=self.collection_ref,
                data=data.model_dump(),
                doc_id=brewery_id,
            )
            print(write_result)

            return data

        @router.get("/{brewery_id}", status_code=200)
        async def get_brewery(brewery_id: str) -> Brewery:
            """Gets a brewery record  
            Args:  
                brewery_id - the id for the brewery document to retrieve

            Returns:  
                a brewery document
            """
            doc = get_doc(collection_ref=self.collection_ref, doc_id=brewery_id)
            brewery = Brewery(**doc)

            return brewery

        return router
