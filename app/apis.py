from fastapi import APIRouter, HTTPException
from .schemas import SingleVideoSchema, PlaylistVideoSchema, ChannelVideoSchema
from .services import (
    youtube_download_single_video,
    youtube_download_playlist,
    youtube_download_channel_videos,
)


router = APIRouter()


@router.post("/single-video/")
async def download_single_video(data: SingleVideoSchema):
    youtube_download_single_video(data.video_url, data.save_path, data.quality, data.types)
    return {"message": f"you will find your video in {data.save_path}"}


@router.post("/playlist/")
async def download_playlist_videos(data: PlaylistVideoSchema):
    youtube_download_playlist(data.playlist_url, data.save_path, data.quality,data.types)
    return {"message": f"you will find your videos in {data.save_path}"}


@router.post("/channel/")
async def download_channel_videos(data: ChannelVideoSchema):
    youtube_download_channel_videos(data.channel_url, data.save_path, data.quality, data.types)
    return {"message": f"you will find your videos in {data.save_path}"}
