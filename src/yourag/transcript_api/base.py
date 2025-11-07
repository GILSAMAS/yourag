from youtube_transcript_api import YouTubeTranscriptApi
from yourag.models.transcript import Transcript, TranscriptEntry
from typing import List, Dict, Any


class TranscriptApi:
    """
    Base class for transcript APIs.
    """

    def __init__(self, video_id: str):
        self.api = YouTubeTranscriptApi()
        self.video_id = video_id

    def get_transcript(self) -> List[Dict[str, Any]]:
        """
        Get the transcript of a YouTube video by its ID.

        :return: The transcript as a list of dictionaries with start time, duration, and text
        """
        try:
            transcript = self.api.fetch(self.video_id)
            processed_transcript = self.__process_transcript(transcript)
            return processed_transcript
        except Exception as e:
            print(f"Error retrieving transcript: {e}")
            return []

    def __process_transcript(self, transcript) -> Transcript:
        """
        Process the transcript into a Transcript object.

        :param transcript: The raw transcript data.
        :return: Transcript object containing the transcript entries.
        """
        entries = [
            TranscriptEntry(start=item.start, duration=item.duration, text=item.text)
            for item in transcript
        ]

        return Transcript(video_id=self.video_id, entries=entries)
