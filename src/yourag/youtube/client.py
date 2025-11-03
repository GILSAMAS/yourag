import os
from googleapiclient.discovery import build
from typing import Optional


class YouTubeClient:
    """
    This class implements a generic YouTube Data API client.
    It provides methods to interact with various YouTube Data API endpoints.
    Users Do not use this class directly; instead, use specific service classes that
    extend this generic client.
    """

    client = None

    def __init__(self, api_key: Optional[str] = None):
        """
        Initializes the YouTube client with the provided API key.

        :param api_key: YouTube Data API key. If not provided, it will be read from the
                        environment variable 'YT_API_KEY'.
        """
        if self.client is not None:
            print("YouTubeClient is already initialized.")
            return  # Client already initialized
        self.api_key = api_key or os.getenv("YT_API_KEY")
        if not self.api_key:
            raise ValueError("No YouTube API key provided.")
        self.client = build("youtube", "v3", developerKey=self.api_key)

    def get_video_details(self, video_id: str):
        """
        Retrieves details of a YouTube video by its ID.

        :param video_id: The ID of the YouTube video.
        :return: Video details as returned by the YouTube Data API.
        """
        return (
            self.client.videos()
            .list(part="snippet,contentDetails,statistics", id=video_id)
            .execute()
        )

    def get_channel_details(self, channel_id: str):
        """
        Retrieves details of a YouTube channel by its ID.

        :param channel_id: The ID of the YouTube channel.
        :return: Channel details as returned by the YouTube Data API.
        """
        return (
            self.client.channels()
            .list(part="snippet,contentDetails,statistics", id=channel_id)
            .execute()
        )

    def get_comments(self, video_id: str, max_results=50):
        """
        Retrieves comments for a YouTube video by its ID.

        :param video_id: The ID of the YouTube video.
        :param max_results: The maximum number of comments to retrieve.
        :return: A list of comments as returned by the YouTube Data API.
        """
        return (
            self.client.commentThreads()
            .list(
                part="snippet",
                videoId=video_id,
                maxResults=max_results,
                textFormat="plainText",
            )
            .execute()
        )
