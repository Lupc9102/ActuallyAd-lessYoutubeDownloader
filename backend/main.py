from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
import os
import uuid

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download")
async def download(request: Request):
    data = await request.json()
    url = data.get("url")
    format = data.get("format")
    if not url or format not in ("mp3", "mp4"):
        return JSONResponse(content={"error": "Invalid input"}, status_code=400)

    uid = str(uuid.uuid4())
    filename = f"downloads/{uid}.%(ext)s"
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": filename,
        "format": "bestaudio/best" if format == "mp3" else "best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio" if format == "mp3" else "FFmpegVideoRemuxer",
            "preferredcodec": "mp3" if format == "mp3" else "mp4",
        }],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    final_ext = "mp3" if format == "mp3" else "mp4"
    final_file = f"downloads/{uid}.{final_ext}"
    return FileResponse(final_file, filename=f"video.{final_ext}", media_type="application/octet-stream")
