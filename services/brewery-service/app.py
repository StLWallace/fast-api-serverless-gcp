from fastapi import FastAPI
from routes.breweries import BreweryRouter
from routes.beers import BeerRouter
from libs.firestore import get_firestore_client, get_firestore_collection
from google.cloud.firestore import CollectionReference
import os


def set_firestore_collection() -> CollectionReference:
    """Establishes a firestore client and collection to be leveraged by the app
    For this app, the collection_name should be set via the COLLECTION_NAME env var
    Returns:
        a Firestore CollectionReference
    """
    firestore_client = get_firestore_client()
    firestore_collection = get_firestore_collection(
        collection_name=os.getenv("COLLECTION_NAME"), client=firestore_client
    )
    return firestore_collection


def create_app(
    firestore_collection: CollectionReference,
    docs_url: str = "/docs",
    openapi_url: str = "/openapi.json",
) -> FastAPI:
    """Configures the FastAPI app
    Args:
        docs_url - the path for the Swagger docs
        openapi_url - path for the openapi spec (used by docs)
        firestore_collection - a Firestore CollectionReference to be leveraged by the application

    Returns:
        a FastAPI object
    """
    app = FastAPI()

    app.include_router(BreweryRouter(firestore_collection).router, prefix="/breweries")
    app.include_router(BeerRouter(firestore_collection).router, prefix="/beers")
    app.docs_url = docs_url
    app.openapi_url = openapi_url

    return app

# Define app and collection
collection_ref = set_firestore_collection()
app = create_app(firestore_collection=collection_ref)
