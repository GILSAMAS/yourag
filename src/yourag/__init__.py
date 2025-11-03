from yourag.utils.file_utils import get_root_project
from yourag.youtube.client import YouTubeClient
from yourag.youtube.video import YTVideo
from dotenv import load_dotenv
import os


def main() -> None:
    # load_dotenv()
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
