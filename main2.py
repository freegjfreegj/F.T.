#!C:\Users\82105\AppData\Local\Programs\Python\Python310\python.exe
print("content-Type: text/html") #header
print() #한줄 뛰우기



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
