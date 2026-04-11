from extractor import get_video_info, extract_formats
from downloader import download_video, download_audio
from selector import (
    get_available_resolutions,
    select_resolution,
    select_video,
    select_audio
)
from converter import (
    process_video_only,
    process_audio_only,
    process_both
)

def select_mode():
    print("\nSelect Mode:")
    print("1. Video only")
    print("2. Audio only")
    print("3. Both")
    
    while True:
        choice = input("Enter choice: ")
        if choice in ["1", "2", "3"]:
            return choice
        print("Invalid choice.")

def main():
    url = input("Enter YouTube URL: ")
    mode = select_mode()
    info = get_video_info(url)
    video_formats, audio_formats = extract_formats(info)

    # VIDEO ONLY or BOTH
    if mode in ["1", "3"]:
        resolutions = get_available_resolutions(video_formats)
        if not resolutions:
            print("❌ High resolution not available")
            return

        selected_res = select_resolution(resolutions)
        video = select_video(video_formats, selected_res)
        if video is None:
            return

        video_path = download_video(url, video)

    # AUDIO ONLY or BOTH
    if mode in ["2", "3"]:
        audio = select_audio(audio_formats)
        if audio is None:
            return

        audio_path = download_audio(url, audio)

    # PROCESSING
    if mode == "1":
        process_video_only(video_path)

    elif mode == "2":
        process_audio_only(audio_path)

    elif mode == "3":
        process_both(video_path, audio_path)

if __name__ == "__main__":
    main()