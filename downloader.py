import yt_dlp
import os
import uuid

TEMP_DIR = "temp"


def ensure_temp_dir():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)


def generate_filename(prefix, ext):
    return f"{prefix}_{uuid.uuid4().hex[:8]}.{ext}"


def download_stream(url, format_id, filename):
    ydl_opts = {
        "format": format_id,
        "outtmpl": os.path.join(TEMP_DIR, filename),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video(url, video_format):
    ensure_temp_dir()

    filename = generate_filename("video", video_format.get("ext", "mp4"))
    print("\n⬇️ Downloading video...")

    download_stream(url, video_format["format_id"], filename)
    return os.path.join(TEMP_DIR, filename)


def download_audio(url, audio_format):
    ensure_temp_dir()

    filename = generate_filename("audio", audio_format.get("ext", "m4a"))
    print("⬇️ Downloading audio...")

    download_stream(url, audio_format["format_id"], filename)
    return os.path.join(TEMP_DIR, filename)