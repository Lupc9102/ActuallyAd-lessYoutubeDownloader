from yt_dlp import YoutubeDL
import os
import uuid

DOWNLOAD_DIR = "downloads"

def download_video(url, format):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    filename = str(uuid.uuid4())
    output_path = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

    ydl_opts = {
        'outtmpl': output_path,
    }

    if format == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        })
    elif format == "mp4":
        ydl_opts.update({'format': 'bestvideo+bestaudio/best'})

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir(DOWNLOAD_DIR):
        if file.startswith(filename):
            return os.path.join(DOWNLOAD_DIR, file)
    return None