from extractor import get_video_info, extract_formats
from downloader import download_video, download_audio
from selector import *
from converter import *

def estimate_size(video, audio, duration):
    bitrate = (video.get("tbr", 0) if video else 0) + (audio.get("abr", 0) if audio else 0)
    if bitrate == 0 or duration == 0:
        return "Unknown"
    return f"{(bitrate * duration) / (8 * 1024):.2f} MB"

def confirm():
    return input("\nProceed? (y/n): ").lower() == "y"

def select_mode():
    print("\nMode:\n1. Video\n2. Audio\n3. Both")
    while True:
        m = input("Choice: ")
        if m in ["1", "2", "3"]:
            return m

def main():
    print("\n==== YouTube Downloader ====\n")
    url = input("Enter URL:\n> ").strip()
    if not url:
        print("Invalid URL")
        return
    print("\nFetching info...")
    info = get_video_info(url)
    video_formats, audio_formats = extract_formats(info)
    duration = info.get("duration", 0)
    mode = select_mode()
    video = None
    audio = None
    res = None
    if mode in ["1", "3"]:
        resolutions = get_available_resolutions(video_formats)
        if not resolutions:
            print("No 1080p+ available")
            return
        res = select_resolution(resolutions)
        video = select_video(video_formats, res)
    if mode in ["2", "3"]:
        audio = select_audio(audio_formats)
    print(f"\nEstimated size: {estimate_size(video, audio, duration)}")
    if not confirm():
        print("Cancelled.")
        return
    if mode in ["1", "3"]:
        video_path = download_video(url, video)
    if mode in ["2", "3"]:
        audio_path = download_audio(url, audio)
    print("\nProcessing...")
    if mode == "1":
        process_video_only(video_path, res)
    elif mode == "2":
        process_audio_only(audio_path)
    else:
        process_both(video_path, audio_path, res)
    print("\nDone!")

if __name__ == "__main__":
    main()