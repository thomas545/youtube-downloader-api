import logging
from fastapi import HTTPException

try:
    from pytube import Playlist, YouTube
    from pytube.exceptions import VideoUnavailable
except ImportError:
    raise ImportError(
        "No module named 'pytube' (pip install pytube) to install the package"
    )

logger = logging.getLogger(__name__)


def progressive(quality):
    return True if quality in ["360p", "480p", "720p", "1080p"] else False


def check_quality(quality):
    available_qualities = [
        "144p",
        "240p",
        "360p",
        "480p",
        "720p",
        "1080p",
    ]

    if quality not in available_qualities:
        raise HTTPException("your quality not supported.")


def youtube_download_single_video(url, output_path, quality="360p"):
    check_quality(quality)

    try:
        yt = YouTube(url)
    except VideoUnavailable:
        raise HTTPException("Video URL invalid.")
    else:
        stream = yt.streams.filter(res=quality, progressive=progressive(quality))
        stream.first().download(output_path=output_path)

    return True


def youtube_download_playlist(playlist_url, output_path, quality="360p"):
    check_quality(quality=quality)

    pl = Playlist(playlist_url)
    failed_videos_url = []

    for url in pl.video_urls:
        try:
            yt = YouTube(url)
        except VideoUnavailable:
            failed_videos_url.append(url)
        else:
            stream = yt.streams.filter(res=quality, progressive=progressive(quality))
            stream.first().download(output_path=output_path)

    if failed_videos_url:
        failed_urls = ", ".join(failed_videos_url)
        return f"Failed Videos URLs are: {failed_urls}"

    return True