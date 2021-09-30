from fastapi import APIRouter
from . import apis

api_router = APIRouter()
api_router.include_router(
    apis.router, prefix="/youtube-downloader", tags=["youtube_downloader"]
)
