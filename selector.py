def get_available_resolutions(video_formats):
    resolutions = sorted(
        list({v["height"] for v in video_formats if v["height"] and v["height"] >= 1080})
    )
    return resolutions

def select_resolution(resolutions):
    print("\nAvailable Resolutions:\n")
    for i, r in enumerate(resolutions):
        print(f"{i}. {r}p")
    while True:
        try:
            choice = int(input("\nSelect resolution: "))
            if 0 <= choice < len(resolutions):
                return resolutions[choice]
        except:
            pass
        print("Invalid choice. Try again.")

# VIDEO SELECTION
def score_video_format(f):
    score = 0
    score += (f.get("tbr") or 0) * 2 # Bitrate (most important)
    vcodec = f.get("vcodec", "") # Codec efficiency (better compression = better visual quality)
    if "av01" in vcodec:
        score += 300
    elif "vp9" in vcodec:
        score += 200
    elif "avc1" in vcodec:
        score += 100
    return score

def select_video(video_formats, selected_resolution):
    candidates = [
        v for v in video_formats
        if v["height"] == selected_resolution
    ]
    if not candidates:
        print("❌ No video found for selected resolution")
        return None
    best = sorted(candidates, key=score_video_format, reverse=True)[0]
    print("\nSelected Video:")
    print(best)
    return best

# AUDIO SELECTION
def score_audio_format(f):
    score = 0
    score += (f.get("abr") or 0) * 2 # Bitrate priority
    acodec = f.get("acodec", "") # Codec preference
    if "mp4a" in acodec:
        score += 200
    elif "opus" in acodec:
        score += 150
    return score

def select_audio(audio_formats):
    if not audio_formats:
        print("❌ No audio formats found")
        return None
    best = sorted(audio_formats, key=score_audio_format, reverse=True)[0]
    print("\nSelected Audio:")
    print(best)
    return best