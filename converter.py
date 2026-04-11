import subprocess
import os

OUTPUT_DIR = "output"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def get_codec(file_path, stream_type):
    stream = "v:0" if stream_type == "video" else "a:0"
    command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", stream,
        "-show_entries", "stream=codec_name",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        return subprocess.check_output(command).decode().strip()
    except:
        return None

#VIDEO ONLY
def process_video_only(video_path, output_name="video.mp4"):
    ensure_output_dir()
    output_path = os.path.join(OUTPUT_DIR, output_name)
    video_codec = get_codec(video_path, "video")
    command = ["ffmpeg", "-y", "-i", video_path]
    if video_codec != "h264":
        command += ["-c:v", "libx264", "-crf", "18", "-preset", "slow"]
    else:
        command += ["-c:v", "copy"]
    command += ["-an", output_path]
    subprocess.run(command)
    print("✅ Video saved:", output_path)

#AUDIO ONLY
def process_audio_only(audio_path, output_name="audio.m4a"):
    ensure_output_dir()
    output_path = os.path.join(OUTPUT_DIR, output_name)
    audio_codec = get_codec(audio_path, "audio")
    command = ["ffmpeg", "-y", "-i", audio_path]
    if audio_codec != "aac":
        command += ["-c:a", "aac", "-b:a", "192k"]
    else:
        command += ["-c:a", "copy"]
    command += ["-vn", output_path]
    subprocess.run(command)
    print("✅ Audio saved:", output_path)

#BOTH VIDEO AND AUDIO
def process_both(video_path, audio_path, output_name="final.mp4"):
    ensure_output_dir()
    output_path = os.path.join(OUTPUT_DIR, output_name)
    video_codec = get_codec(video_path, "video")
    audio_codec = get_codec(audio_path, "audio")
    command = ["ffmpeg", "-y", "-i", video_path, "-i", audio_path]

    # Video
    if video_codec != "h264":
        command += ["-c:v", "libx264", "-crf", "18", "-preset", "slow"]
    else:
        command += ["-c:v", "copy"]

    # Audio
    if audio_codec != "aac":
        command += ["-c:a", "aac", "-b:a", "192k"]
    else:
        command += ["-c:a", "copy"]

    command.append(output_path)
    subprocess.run(command)
    print("✅ Final video:", output_path)