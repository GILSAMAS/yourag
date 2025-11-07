from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import timedelta


class TranscriptEntry(BaseModel):
    text: str
    start: timedelta
    end: Optional[timedelta] = None
    duration: timedelta


class Transcript(BaseModel):
    video_id: str
    language: Optional[str] = None
    entries: List[TranscriptEntry] = Field(default_factory=list)

