from fastapi import FastAPI, Depends
from routes.breweries import BreweryRouter
from libs.firestore import get_firestore_client, get_firestore_collection
from google.cloud.firestore import CollectionReference
import os


def set_firestore_collection():
    firestore_client = get_firestore_client()
    firestore_collection = get_firestore_collection(
        collection_name=os.getenv("COLLECTION_NAME"), client=firestore_client
    )
    return firestore_collection


def create_app(
    docs_url: str = "/docs",
    openapi_url: str = "openapi.json",
    firestore_collection: CollectionReference = set_firestore_collection(),
) -> FastAPI:
    """Configures the FastAPI"""
    app = FastAPI()

    app.include_router(BreweryRouter(firestore_collection).router, prefix="/breweries")
    app.docs_url = docs_url
    app.openapi_url = openapi_url

    return app


app = create_app()
