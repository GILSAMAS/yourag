from yourag.vector_stores.chroma_store import ChromaVectorStore
from typing import Optional
from pprint import pprint


def list_collections() -> None:
    """
    List all collections in the vector store.
    """
    store = ChromaVectorStore()
    collections = store.list_collections()
    if not collections:
        print("No collections found in the vector store.")
        return
    print("Collections in the vector store:")
    for collection_name in collections:
        collection = store.get_or_create_collection(collection_name)
        pprint(collection.metadata, indent=4)
        print("-" * 40)
