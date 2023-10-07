from fastapi import FastAPI
from routes.breweries import brewery_router


def create_app(docs_url: str = "/docs", openapi_url: str = "openapi.json") -> FastAPI:
    """Configures the FastAPI"""
    app = FastAPI()
    app.include_router(brewery_router, prefix="/breweries")
    app.docs_url = docs_url
    app.openapi_url = openapi_url

    return app


app = create_app()
