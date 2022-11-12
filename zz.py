#!C:\Users\82105\AppData\Local\Programs\Python\Python310\python.exe
print("content-Type: text/html")
print()

import os
import pytube
from pytube.cli import on_progress

url = "https://www.youtube.com/watch?v=80QDPaNMcTo"

yt = pytube.YouTube(url, on_progress_callback=on_progress)
print(yt.streams)

save_dir = "./" # 저장경로

yt.streams.filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()\
    .download(save_dir)
