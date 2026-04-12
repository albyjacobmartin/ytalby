# YTAlby - YouTube Downloader (CLI)

A fast and clean YouTube downloader built with Python.

---

## Features

- Video only (MP4 container - H.264 codec)
- Audio only (M4A container - AAC codec)
- Video + Audio merge (MP4 container - H.264 and AAC codec)
- Resolution selection (1080p and above)
- Automatic conversion using FFmpeg
- Clean CLI interface
- Safe processing (no corrupted files)
- Temporary file cleanup

---

## Download

Go to the **Releases** section of this repository and download the latest version:

- https://github.com/albyjacobmartin/ytalby/releases/latest

---

## Requirements

### 1. FFmpeg (MANDATORY)

Install FFmpeg and add it to PATH.

#### Windows (Command Prompt):

```bash
winget install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
```

---

## Usage

1. Download `ytalby.exe` from Releases
2. Run (double click the .exe file):

```bash
ytalby.exe
```

3. Follow instructions:
   - Enter YouTube URL
   - Select mode (video/audio/both)
   - Select resolution
   - Confirm download

---

## 📁 Output

Downloaded files will be saved in:

```
output/
 ├── final_1080.mp4
 ├── final_1440.mp4
 ├── final_audio.m4a
```

---

## How It Works

1. Extract formats using yt-dlp  
2. Select best streams  
3. Download video & audio  
4. Convert to:
   - H.264 (video)
   - AAC (audio)  
5. Merge into MP4  

---

## Development

Run locally:

```bash
python main.py
```

---

## Build EXE

```bash
pyinstaller --onefile --name ytalby --collect-all yt_dlp main.py
```

---

## Notes

- Only resolutions **≥1080p** are supported
- Conversion may take time for high-resolution videos
- FFmpeg must be installed

---

## From Author

If you are having any issues/confusion, feel free to contact me through LinkedIn.

If you like this project, please star this project.