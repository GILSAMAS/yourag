from yourag.youtube.video import YTVideo
from yourag.transcript.base import TranscriptParser
from yourag.ai.embeddings import EmbeddingFactory
from yourag.ai.generators import GeneratorFactory
from yourag.vector_stores.chroma_store import ChromaVectorStore
from dotenv import load_dotenv

def query_video(video_id: str, query_text: str):
    """
    Query a YouTube video by its ID and a text query.

    :param video_id: The ID of the YouTube video to query.
    :param query_text: The text query to search within the video content.
    :return: None
    """
    print(f"Querying video with ID: {video_id} for query: '{query_text}'")
    load_dotenv()

    embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    generator = GeneratorFactory.get_generator("openai")
    chroma_store = ChromaVectorStore()
    collection_name = f"video_{video_id}"
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
    