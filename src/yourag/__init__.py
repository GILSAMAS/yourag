from yourag.utils.file_utils import get_root_project
from yourag.youtube.client import YouTubeClient
from yourag.youtube.video import YTVideo
from yourag.vector_stores.chroma_store import ChromaVectorStore
from yourag.ai.embeddings import EmbeddingFactory
from yourag.ai.generators import GeneratorFactory
from dotenv import load_dotenv
import os


def main() -> None:
    load_dotenv()
    embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    generator = GeneratorFactory.get_generator("openai")

    question = "What is the capital of France?"
    context = "France is a country in Europe."
    answer = generator.generate_answer(question, context)
    print("Generated Answer:")
    print(answer)

    # chroma_store = ChromaVectorStore()

    # creating a new collection
    # ids = ["vec1", "vec2", "vec3"]
    # embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    # documents = ["Document 1", "Document 2", "Document 3"]
    # metadatas = [{"source": "doc1"}, {"source": "doc2"}, {"source": "doc3"}]
    # collection_name = "test_collection"
    # # Use the chroma_store for vector operations
    # chroma_store.add_vectors(
    #     ids=ids,
    #     embeddings=embeddings,
    #     documents=documents,
    #     collection_name=collection_name,
    #     metadatas=metadatas,
    # )
    # query_vector = [0.1, 0.2, 0.3]
    # top_k = 2
    # collection_name = "test_collection"
    # results = chroma_store.query_vectors(
    #    query_vector=query_vector, top_k=top_k, collection_name=collection_name
    # )
    # print("QUERY RESULTS:")
    # print(results)
    # # for result in results:
    # #     print(result)


def main2() -> None:
    load_dotenv()
    yt_client = YouTubeClient()
    yt_video = YTVideo("_kvuw74LnTw", yt_client)
    # yt_video.post_comment(text="This is a test comment!")
    comment_id = "UgzfFDZ_4qQLr7FmHcN4AaABAg"
    yt_video.post_comment(comment_id=comment_id, text="This is a test reply!")
    # transcript = yt_video.get_transcript()

    # print("VIDEO TRANSCRIPT:")
    # print("Language:", transcript.language)
    # for entry in transcript.entries:
    #     print("-" * 40)
    #     print(f"[{entry.start} --> {entry.end}] ({entry.duration}): {entry.text}")
    # print([t for t in transcript][0])
    # # details = yt_video.details
    # # print(details)
    # statistics = yt_video.get_statistics()
    # print("VIDEO STATISTICS:")
    # print(f"Views: {statistics.view_count}")
    # print(f"Likes: {statistics.like_count}")
    # print(f"Dislikes: {statistics.dislike_count}")
    # print(f"Comments: {statistics.comment_count}")

    comments = yt_video.get_comments(max_results=20)
    print("TOTAL COMMENTS RETRIEVED:", comments.total_comments)
    print("VIDEO ID:", comments.video_id)
    print("\nVIDEO COMMENTS:")
    for comment in comments.comments:
        print("-" * 40)
        print(
            f"- {comment.author}: {comment.text} (Likes: {comment.like_count}, ID: {comment.comment_id})"
        )

    # print("Hello from yourag!")
    # metadata = yt_video.get_metadata()
    # print("TITLE:")
    # print(metadata.title)
    # print("PUBLISH DATE:")
    # print(metadata.publish_date)
    # print("CHANNEL TITLE:")
    # print(metadata.channel_title)
    # print("VIDEO ID:")
    # print(metadata.video_id)
    # print("VIDEO TAGS:")
    # print(metadata.tags)
    # print("METADATA TYPE:")
    # print(type(metadata).__name__)
