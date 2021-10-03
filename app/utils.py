def print_progressbar(total, current, barsize=60):
    progress = int(current * barsize / total)
    completed = str(int(current * 100 / total) + 1) + "%"
    print(
        "[",
        chr(9608) * progress,
        " ",
        completed,
        "." * (barsize - progress),
        "] ",
        str(current) + "/" + str(total),
        sep="",
        end="\r",
        flush=True,
    )


def download_time(content_length, video_title):
    total = int(content_length)
    barsize = 60
    print_frequency = max(min(total // barsize, 100), 1)
    print(f"Start Download {video_title}", flush=True)
    for i in range(1, total + 1):
        if i % print_frequency == 0 or i == 1:
            print_progressbar(total, i, barsize)
    print("\nFinished", flush=True)


def get_dwonload_progressbar(video, quality):
    content_length = 0
    formats = video.vid_info.get("streamingData", {}).get("formats", [])
    for format in formats:
        if format.get("qualityLabel") == quality:
            content_length = format.get("contentLength")
    if content_length:
        download_time(content_length, video.title)
