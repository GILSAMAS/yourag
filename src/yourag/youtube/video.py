from .client import YouTubeClient
from .models import VideoMetadata
from .models import VideoStatistics
from .models import VideoComment
from .models import Comments


class YTVideo:
    def __init__(self, video_id: str, client: YouTubeClient):
        self.video_id = video_id
        self.client = client
        self._details = None

    @property
    def details(self):
        if self._details is None:
            self._details = self.client.get_video_details(self.video_id)
        return self._details

    def get_metadata(self) -> VideoMetadata:
        """
        Gets the metadata of the YouTube video.

        :return VideoMetadata: Metadata of the video.
        """
        item = self.details["items"][0]["snippet"]
        return VideoMetadata(
            video_id=self.video_id,
            title=item["title"],
            description=item.get("description"),
            publish_date=item["publishedAt"],
            channel_id=item["channelId"],
            channel_title=item["channelTitle"],
            tags=item.get("tags"),
        )

    def get_statistics(self) -> VideoStatistics:
        """
        Gets the statistics of the YouTube video.

        :return VideoStatistics: Statistics of the video.
        """
        stats = self.details["items"][0]["statistics"]
        return VideoStatistics(
            view_count=int(stats.get("viewCount", 0)),
            like_count=int(stats.get("likeCount", 0)),
            dislike_count=int(stats.get("dislikeCount", 0)),
            comment_count=int(stats.get("commentCount", 0)),
        )

    def get_comments(self, max_results=50) -> Comments:
        """
        Gets the comments of the YouTube video.

        :param max_results: Maximum number of comments to retrieve.
        :return Comments: Comments of the video.
        """
        response = self.client.get_comments(self.video_id, max_results)
        comments_list = []
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments_list.append(
                VideoComment(
                    video_id=self.video_id,
                    comment_id=item["id"],
                    author=comment["authorDisplayName"],
                    text=comment["textDisplay"],
                    like_count=int(comment.get("likeCount", 0)),
                    published_at=comment["publishedAt"],
                )
            )
        total_comments = int(response["pageInfo"].get("totalResults", 0))
        return Comments(
            video_id=self.video_id,
            total_comments=total_comments,
            comments=comments_list,
        )
