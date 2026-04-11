import yt_dlp
import os


TEMP_DIR = "temp"


def ensure_temp_dir():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)


def download_stream(url, format_id, filename):
    ydl_opts = {
        "format": format_id,
        "outtmpl": os.path.join(TEMP_DIR, filename),
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video(url, video_format):
    ext = video_format.get("ext", "mp4")
    filename = f"video.{ext}"

    print("\n⬇️ Downloading video...")
    download_stream(url, video_format["format_id"], filename)

    return os.path.join(TEMP_DIR, filename)


def download_audio(url, audio_format):
    ext = audio_format.get("ext", "m4a")
    filename = f"audio.{ext}"

    print("\n⬇️ Downloading audio...")
    download_stream(url, audio_format["format_id"], filename)

    return os.path.join(TEMP_DIR, filename)