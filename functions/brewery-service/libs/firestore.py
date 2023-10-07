import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import Client
from typing import List

# Use the application default credentials.
def get_firestore_client() -> Client:
    """Initializes a Firestore client"""
    cred = credentials.ApplicationDefault()

    firebase_admin.initialize_app(cred)
    client = firestore.client()

    return client


def get_docs(client: Client, collection: str) -> List[dict]:
    """gets all documents for a collection
    args:
        client - a Firestore client
        collection - the Firestore collection to query
    
    returns:
        a list of dicts containing the docs in the collection
    """
    collection_ref = client.collection(collection)
    docs = collection_ref.stream()

    return [doc.to_dict() for doc in docs]


if __name__ == "__main__":

    client = get_firestore_client()

    dox = get_docs(client=client, collection="bankers-residents")

    print(dox)
