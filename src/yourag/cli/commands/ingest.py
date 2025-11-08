from yourag.youtube.client import YouTubeClient
from yourag.youtube.video import YTVideo
from yourag.transcript.base import TranscriptParser
from yourag.ai.embeddings import EmbeddingFactory
from yourag.vector_stores.chroma_store import ChromaVectorStore
from dotenv import load_dotenv
import os
import uuid
from typing import Dict, List


def ingest_video(video_id: str, name: str) -> None:
    """
    This function ingests a Youtube Video by its ID,
    it creates a collection in Chroma vector store with the transcript chunks embeddings.

    :param name: The name to assign to the video collection.
    :param video_id: The ID of the YouTube video to ingest.
    :return: None
    """
    load_dotenv()
    print("Ingesting video with ID:", video_id)
    yt_client = YouTubeClient()
    video = YTVideo(video_id=video_id, client=yt_client)
    video_metadata = video.get_metadata()
    print(f"Retrieved video: {video_metadata.title} by {video_metadata.channel_title}")
    transcript = video.get_transcript()
    parser = TranscriptParser(transcript)
    chunks = parser.get_chunks(chunk_size=80, overlap=0.1)
    embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    chroma_store = ChromaVectorStore()
    collection_name = f"video_{video.video_id}"
    # First check if collection exists, if so, skip ingestion
    embeddings = _get_embeddings_dict(chunks, embedding_generator)
    chroma_store.add_vectors(
        ids=embeddings["ids"],
        embeddings=embeddings["embeddings"],
        documents=embeddings["documents"],
        collection_name=collection_name,
        metadatas=embeddings["metadatas"],
        collection_metadata={
            "video_title": video_metadata.title,
            "channel_title": video_metadata.channel_title,
            "video_id": video.video_id,
            "name": name  # corresponds to provided name argument
        },
    )


def _get_embeddings_dict(chunks, embedding_generator) -> Dict[str, List]:
    """
    Helper function to generate embeddings dict from chunks.

    :param chunks: List of transcript chunks.
    :param embedding_generator: The embedding generator instance.
    :return: embeddings dict
    """
    embeddings = {
        "ids": [],
        "embeddings": [],
        "documents": [],
        "metadatas": [],
    }
    for chunk in chunks:
        embedding = embedding_generator.generate_embeddings(chunk["text"])
        embeddings["ids"].append(str(uuid.uuid4()))
        embeddings["embeddings"].append(embedding)
        embeddings["documents"].append(chunk["text"])
        embeddings["metadatas"].append(
            {
                "start": str(chunk["start"]),
                "end": str(chunk["end"]),
                "duration": str(chunk["duration"]),
            }
        )

    return embeddings
