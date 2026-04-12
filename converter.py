import subprocess
import os

OUTPUT_DIR = "output"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def get_codec(file_path, stream):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", stream,
        "-show_entries", "stream=codec_name",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        return subprocess.check_output(cmd).decode().strip()
    except:
        return None

def run_ffmpeg(cmd):
    try:
        subprocess.run(cmd, check=True)
        return True
    except:
        print("FFmpeg failed")
        return False

def finalize(temp, final):
    if os.path.exists(temp):
        os.rename(temp, final)

def cleanup(*files):
    for f in files:
        if f and os.path.exists(f):
            os.remove(f)

#VIDEO
def process_video_only(video_path, res):
    ensure_output_dir()
    final = os.path.join(OUTPUT_DIR, f"final_{res}.mp4")
    temp = final + ".part"
    vcodec = get_codec(video_path, "v:0")
    cmd = ["ffmpeg", "-y", "-i", video_path]
    if vcodec != "h264":
        cmd += ["-c:v", "libx264", "-crf", "18", "-preset", "slow"]
    else:
        cmd += ["-c:v", "copy"]
    cmd += ["-an", "-f", "mp4", temp]
    print("\nProcessing video...")
    if run_ffmpeg(cmd):
        finalize(temp, final)
        print("Saved:", final)
    cleanup(video_path)

#AUDIO
def process_audio_only(audio_path):
    ensure_output_dir()
    final = os.path.join(OUTPUT_DIR, "final_audio.m4a")
    temp = final + ".part"
    acodec = get_codec(audio_path, "a:0")
    cmd = ["ffmpeg", "-y", "-i", audio_path]
    if acodec != "aac":
        cmd += ["-c:a", "aac", "-b:a", "192k"]
    else:
        cmd += ["-c:a", "copy"]
    cmd += ["-vn", "-f", "mp4", temp]
    print("\nProcessing audio...")
    if run_ffmpeg(cmd):
        finalize(temp, final)
        print("Saved:", final)
    cleanup(audio_path)

#BOTH
def process_both(video_path, audio_path, res):
    ensure_output_dir()
    final = os.path.join(OUTPUT_DIR, f"final_{res}.mp4")
    temp = final + ".part"
    vcodec = get_codec(video_path, "v:0")
    acodec = get_codec(audio_path, "a:0")
    cmd = ["ffmpeg", "-y", "-i", video_path, "-i", audio_path]
    cmd += ["-c:v", "copy"] if vcodec == "h264" else ["-c:v", "libx264", "-crf", "18", "-preset", "slow"]
    cmd += ["-c:a", "copy"] if acodec == "aac" else ["-c:a", "aac", "-b:a", "192k"]
    cmd += ["-f", "mp4", temp]
    print("\nProcessing video + audio...")
    if run_ffmpeg(cmd):
        finalize(temp, final)
        print("Saved:", final)
    cleanup(video_path, audio_path)