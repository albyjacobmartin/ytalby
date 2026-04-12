def get_available_resolutions(video_formats):
    return sorted(
        list({v["height"] for v in video_formats if v["height"] and v["height"] >= 1080})
    )

def select_resolution(resolutions):
    print("\nAvailable Resolutions:")
    for i, r in enumerate(resolutions):
        print(f"{i}. {r}p")
    while True:
        try:
            choice = int(input("\nSelect resolution: "))
            if 0 <= choice < len(resolutions):
                return resolutions[choice]
        except:
            pass
        print("Invalid choice.")

#VIDEO
def score_video_format(f):
    score = (f.get("tbr") or 0) * 2
    vcodec = f.get("vcodec", "")
    if "av01" in vcodec:
        score += 300
    elif "vp9" in vcodec:
        score += 200
    elif "avc1" in vcodec:
        score += 100
    return score

def select_video(video_formats, resolution):
    candidates = [v for v in video_formats if v["height"] == resolution]
    if not candidates:
        print("❌ No video found")
        return None
    best = sorted(candidates, key=score_video_format, reverse=True)[0]
    print(f"\nSelected Video: {best['height']}p | {best['vcodec']}")
    return best

#AUDIO
def score_audio_format(f):
    score = (f.get("abr") or 0) * 2
    acodec = f.get("acodec", "")
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
    print(f"Selected Audio: {best['acodec']} ({best['abr']} kbps)")
    return best