from fastapi import APIRouter, HTTPException
from .schemas import SingleVideoSchema, PlaylistVideoSchema
from .services import youtube_download_single_video, youtube_download_playlist


router = APIRouter()


@router.post("/single-video/")
async def download_single_video(data: SingleVideoSchema):
    youtube_download_single_video(data.video_url, data.save_path, data.quality)
    return {"message": f"you will find your video in {data.save_path}"}


@router.post("/playlist/")
async def download_playlist_videos(data: PlaylistVideoSchema):
    youtube_download_playlist(data.playlist_url, data.save_path, data.quality)
    return {"message": f"you will find your videos in {data.save_path}"}
