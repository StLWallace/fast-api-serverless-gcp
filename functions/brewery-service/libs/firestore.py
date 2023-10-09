import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import Client, CollectionReference
from google.cloud.firestore_v1.types import WriteResult
from typing import List

# Use the application default credentials.
def get_firestore_client() -> Client:
    """Initializes a Firestore client"""
    cred = credentials.ApplicationDefault()

    firebase_admin.initialize_app(cred)
    client = firestore.client()

    return client


def get_firestore_collection(
    collection_name: str, client: Client = None
) -> CollectionReference:
    """Initializes a collection reference"""
    if client is None:
        client = get_firestore_client()
    collection_ref = client.collection(collection_name)

    return collection_ref


def get_docs(collection_ref: CollectionReference) -> List[dict]:
    """gets all documents for a collection
    args:
        collection_ref - a Firestore collection reference
    
    returns:
        a list of dicts containing the docs in the collection
    """
    docs = collection_ref.stream()

    return [doc.to_dict() for doc in docs]


def create_doc(
    collection_ref: CollectionReference, data: dict, doc_id: str = None
) -> WriteResult:
    """Creates a new document in a collection
    Args:
        collection_ref - a Firestore collection reference
        data - a dict of the document to be written
        doc_id (optional) - the unique id for the document. If None, a random ID will be generated

    Returns:
        a WriteResult object

    """
    doc_ref = collection_ref.document(doc_id)
    write_result = doc_ref.set(data)

    return write_result


def get_doc(collection_ref: CollectionReference, doc_id: str) -> dict:
    """Queries a collection for a given document
    Args:
        collection_ref - a Firestore collection reference
        doc_id - the id for the document to retrieve

    Returns:
        a dict containing the document
    """
    doc_ref = collection_ref.document(document_id=doc_id).get()

    return doc_ref.to_dict()
