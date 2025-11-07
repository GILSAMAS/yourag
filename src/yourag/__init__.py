from yourag.utils.file_utils import get_root_project
from yourag.vector_stores.chroma_store import ChromaVectorStore
from yourag.ai.embeddings import EmbeddingFactory
from yourag.ai.generators import GeneratorFactory
from yourag.transcript_api.base import TranscriptApi,TranscriptParser
from dotenv import load_dotenv
import os
import uuid

def main() -> None:
    load_dotenv()
    tapi = TranscriptApi(video_id="_kvuw74LnTw")
    transcript = tapi.get_transcript()
    parser = TranscriptParser(transcript)

    embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    generator = GeneratorFactory.get_generator("openai")
    chroma_store = ChromaVectorStore()
    chunks = parser.get_chunks(chunk_size=50, overlap=0.2)
    embeddings =  {
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
        embeddings["metadatas"].append({"start": chunk["start"], "end": chunk["end"]})

    collection_name = f"video_{tapi.video_id}"
    # Use the chroma_store for vector operations
    # chroma_store.add_vectors(
    #     ids=embeddings["ids"],
    #     embeddings=embeddings["embeddings"],
    #     documents=embeddings["documents"],
    #     collection_name=collection_name,
    #     metadatas=embeddings["metadatas"],
    # )

    # Querying example
    query_text = "What is the main topic of the video?"
    query_embedding = embedding_generator.generate_embeddings(query_text)
    results = chroma_store.query_vectors(
        query_vector=query_embedding,
        top_k=3,
        collection_name=collection_name,
    )
    # print("Relevant documents:", results)
    print(len(results["documents"]))
    for result in results["documents"]:
        print(result)
        print("----")
    
    context = " ".join([text for doc in results["documents"] for text in doc])
    answer = generator.generate_answer(question=query_text, context=context)
    print("Generated Answer:", answer)
    # # Generating text based on retrieved documents
    # context = " ".join([doc["document"] for doc in results])
    # answer = generator.generate_answer(question=query_text, context=context)




