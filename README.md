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

0. Create a folder.
1. Download `ytalby.exe` from **Releases** to that folder
2. Run (double click the .exe file):

```bash
ytalby.exe
```
3. When you download and run the release version, windows defender will give a pop up "unrecognized app". Click on "More info", then click on "Run anyway". It will open terminal.

4. Follow instructions:
   - Enter YouTube URL
   - Select mode (video/audio/both)
   - Select resolution
   - Confirm download

5. Once the download is completed, two folders will be generated in the folder: Output and Temp. The Output folder will store the final video or audio file, while the Temp folder will hold the raw downloaded data. This temporary data is used to process and create the final file, after which it will be automatically removed from the Temp folder.
---

## Output

Downloaded files will be saved in:

```
output/
 ├── final_1080.mp4
 ├── final_1440.mp4
 ├── final_audio.m4a
```

---

## Alternate usage method (if you are a dev)

### Step 0:

Clone this repo to your device.

### Step 1:

In **converter.py**, modify:

from:
```bash
OUTPUT_DIR = "output"
```
to:
```bash
OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "Desktop")
```
### Step 2:

In **ytdwnldr.bat**, update:

```bash
cd /d "C:\Users\updatethispath\ytalby"
```

### Step 3:

- Create a shortcut for **ytdwnldr.bat** on Desktop.

- Right click on the shortcut, then click on Properties.

- Click on change icon, a pop up will come, click on OK.

- Another pop up will come, click on Browse.

- select **YouTube_icon.ico** from the folder, click on OK, then Apply, then again OK.
---
### Result:

Now you will have a shortcut on Desktop with YouTube icon. when you double click on that shortcut, the terminal will open and you can follow the instruction to download the video or audio that you want. The final file will be saved on Desktop (for easy access). Now you are running from Desktop, and the result will also be saved in Desktop.

---
## How It Works

1. Extract formats using yt-dlp.
2. Select best streams.
3. Download video & audio.
4. Convert to:
   - H.264 (video)
   - AAC (audio)  
5. Merge into MP4 container.

---

## Notes

- Only resolutions **≥1080p** are supported.
- Conversion may take time for high-resolution videos.
- FFmpeg must be installed.

---

## Message from Author
If you are having any issues/confusion, feel free to contact me through LinkedIn.

If you like this project, support by giving a star for this repo.