def query_video(video_id: str, query_text: str):
    """
    Query a YouTube video by its ID and a text query.

    :param video_id: The ID of the YouTube video to query.
    :param query_text: The text query to search within the video content.
    :return: None
    """
    print(f"Querying video with ID: {video_id} for query: '{query_text}'")
    # from yourag.youtube.video import YTVideo
    # from yourag.transcript.base import TranscriptParser
    # from yourag.ai.embeddings import EmbeddingFactory
    # from yourag.ai.generator import GeneratorFactory
    # from yourag.vector_stores.chroma_store import ChromaVectorStore

    # load_dotenv()
    # yt_client = YouTubeClient()
    # video = YTVideo(video_id=video_id, client=yt_client)
    # transcript = video.get_transcript()

    # print(f"Transcript for video ID {video.video_id}:")
    # for entry in transcript.entries:
    #     print(f"[{entry.start} - {entry.end}]: {entry.text} - Duration: {entry.duration}\n")

    # parser = TranscriptParser(transcript)
    # chunks = parser.get_chunks(chunk_size=50, overlap=0.2)
    # print(f"Generated {len(chunks)} chunks from the transcript.")
    # for chunk in chunks:
    #     print(f"Duration: {chunk['duration']} - [{chunk['start']} - {chunk['end']}]: {chunk['text']}\n")
    # embedding_generator = EmbeddingFactory.get_embedding_generator("openai")
    # generator = GeneratorFactory.get_generator("openai")
    # chroma_store = ChromaVectorStore()
    # chunks = parser.get_chunks(chunk_size=50, overlap=0.2)

    # collection_name = f"video_{video.video_id}"
    # # Use the chroma_store for vector operations

    # # Querying example
    # query_embedding = embedding_generator.generate_embeddings(query_text)
    # results = chroma_store.query_vectors(
    #     query_vector=query_embedding,
    #     top_k=3,
    #     collection_name=collection_name,
    # )
    # print(len(results["documents"]))
    # for result in results["documents"]:
    #     print(result)
    #     print("----")
    
    # context = " ".join([text for doc in results["documents"] for text in doc])
    # answer = generator.generate_answer(question=query_text, context=context)
    # print("Generated Answer:", answer)
    # # Generating text based on retrieved documents
    # print("Context for answer generation:", context)
    # answer =