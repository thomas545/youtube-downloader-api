from typing import Optional
from pydantic import BaseModel


class SingleVideoSchema(BaseModel):
    save_path: str
    video_url: str
    quality: Optional[str] = "144p"
    types: Optional[str] = "video"


class PlaylistVideoSchema(BaseModel):
    save_path: str
    playlist_url: str
    quality: Optional[str] = "144p"
    types: Optional[str] = "video"

class ChannelVideoSchema(BaseModel):
    save_path: str
    channel_url: str
    quality: Optional[str] = "144p"
    types: Optional[str] = "video"
