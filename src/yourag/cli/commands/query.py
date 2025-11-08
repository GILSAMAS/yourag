from yourag.youtube.video import YTVideo
from yourag.transcript.base import TranscriptParser
from yourag.ai.embeddings import EmbeddingFactory
from yourag.ai.generators import GeneratorFactory
from yourag.vector_stores.chroma_store import ChromaVectorStore
from dotenv import load_dotenv
from typing import Optional


def query_video(video_id: str, query_text: str, name: Optional[str] = None) -> None:
    """
    Query a YouTube video by its ID and a text query.

    :param video_id: The ID of the YouTube video to query.
    :param query_text: The text query to search within the video content.
    :param name: The name of the video collection to query.
    :return: None
    """
    print(f"Querying video with ID: {video_id} for query: '{query_text}'")
    load_dotenv()
    if not video_id and not name:
        raise ValueError("Either video_id or name must be provided to query a video.")

    # if video_id is not provided, retrieve all collections and find by name

    embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    generator = GeneratorFactory.get_generator("openai")
    chroma_store = ChromaVectorStore()
    if video_id is None:
        collections = chroma_store.list_collections()
        matched_collection = None
        for collection_name in collections:
            collection = chroma_store.get_or_create_collection(collection_name)
            if collection.metadata.get("name") == name:
                matched_collection = collection_name
                break
        if not matched_collection:
            raise ValueError(f"No collection found with name: {name}")

        collection_name = matched_collection
    else:
        collection_name = f"video_{video_id}"  # default naming convention
    # Querying example
    query_embedding = embedding_generator.generate_embeddings(query_text)
    results = chroma_store.query_vectors(
        query_vector=query_embedding,
        top_k=3,
        collection_name=collection_name,
    )
    context = " ".join([text for doc in results["documents"] for text in doc])
    answer = generator.generate_answer(question=query_text, context=context)
    print("Answer:", answer)
