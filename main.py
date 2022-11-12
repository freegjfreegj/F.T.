#!C:\Users\82105\AppData\Local\Programs\Python\Python310\python.exe
print("content-Type: text/html") #header
print() #한줄 뛰우기

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

print('''<!doctype html>
<html>

<head>
    <title>TubeMeDown</title>
    <meta charset="utf-8">
</head>

<body>

    <h1><a href="main.py" id="active">TubeMeDown</a></h1>
    <div id="grid">
  <ol>
    <input type="text" placeholder="Link">
    <p>
        <select name='extension'>
        <option value='' selected>-extension-</option>
        <option value='mp3'>mp3</option>
        <option value='wav'>wav</option>
        <option value='mp4'>mp4</option>
        <option value='webm'>webm</option>
        </select>
        <select name='quality'>
        <option value='' selected>-quality-</option>
        <option value='320'>320kbs</option>
        <option value='256'>256kbs</option>
        <option value='192'>192kbs</option>
        <option value='1080'>1080p</option>
        <option value='720'>720p</option>
        <option value='480'>480p</option>
        <option value='360'>360p</option>
        </select>
    </p>
    <p><a href="Download.py">Download</a></p>
  </ol>

</body>

</html>
''')
