import threading
import logging
from fastapi import HTTPException

try:
    from pytube import Playlist, YouTube, Channel
    from pytube.exceptions import VideoUnavailable
except ImportError:
    raise ImportError(
        "No module named 'pytube' (pip install pytube) to install the package"
    )
from .utils import get_dwonload_progressbar


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
        raise HTTPException(status_code=400, detail="Video URL invalid.")
    else:
        stream = yt.streams.filter(res=quality, progressive=progressive(quality))
        # stream.first().download(output_path=output_path)
        file_name, ext = stream.first().default_filename.split(".")
        threading.Thread(
            target=stream.first().download,
            kwargs={
                "output_path": output_path,
            },
        ).start()
        get_dwonload_progressbar(yt, quality)

    return True


def youtube_download_playlist(playlist_url, output_path, quality="360p"):
    check_quality(quality=quality)

    pl = Playlist(playlist_url)
    failed_videos_url = []
    counter = 1

    for url in pl.video_urls[:1]:
        try:
            yt = YouTube(url)
        except VideoUnavailable:
            failed_videos_url.append(url)
        else:
            stream = yt.streams.filter(res=quality, progressive=progressive(quality))
            file_name, ext = stream.first().default_filename.split(".")
            # stream.first().download(
            #     output_path=output_path,
            #     filename=f"{file_name}_{counter}",
            # )

            threading.Thread(
                target=stream.first().download,
                kwargs={
                    "output_path": output_path,
                    "filename": f"{file_name}_{counter}",
                },
            ).start()
            get_dwonload_progressbar(yt, quality)
            counter += 1

    if failed_videos_url:
        failed_urls = "\n ".join(failed_videos_url)
        return f"Failed Videos URLs are: {failed_urls}"

    return True


def youtube_download_channel_videos(channel_url, output_path, quality="360p"):
    check_quality(quality=quality)

    channel = Channel(channel_url)
    failed_videos_url = []

    for url in channel.video_urls:
        try:
            yt = YouTube(url)
        except VideoUnavailable:
            failed_videos_url.append(url)
        else:
            stream = yt.streams.filter(res=quality, progressive=progressive(quality))
            # stream.first().download(output_path=output_path)
            threading.Thread(
                target=stream.first().download,
                kwargs={
                    "output_path": output_path,
                },
            ).start()
            get_dwonload_progressbar(yt, quality)

    if failed_videos_url:
        failed_urls = "\n ".join(failed_videos_url)
        return f"Failed Videos URLs are: {failed_urls}"

    return True
