import yt_dlp

def get_video_info(url: str):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info

def extract_formats(info):
    formats = info.get("formats", [])
    video_formats = []
    audio_formats = []
    for f in formats:
        # Video formats
        if f.get("vcodec") != "none":
            video_formats.append({
                "format_id": f.get("format_id"),
                "ext": f.get("ext"),
                "height": f.get("height"),
                "vcodec": f.get("vcodec"),
                "acodec": f.get("acodec"),
                "tbr": f.get("tbr"),
            })

        # Audio formats
        if f.get("acodec") != "none" and f.get("vcodec") == "none":
            audio_formats.append({
                "format_id": f.get("format_id"),
                "ext": f.get("ext"),
                "acodec": f.get("acodec"),
                "abr": f.get("abr"),
            })
    return video_formats, audio_formats