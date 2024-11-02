
import yt_dlp

url = "https://www.youtube.com/watch?v=MvsAesQ-4zA"
ydl_opts = {'format': 'best'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
