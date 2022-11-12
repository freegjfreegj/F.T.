import cgi, os, view, html_sanitizer, pytube

sanitizer = html_sanitizer.Sanitizer()
sanitizer.sanitize

yt = YouTube(‘’)

stream_video = yt.streams.get_by_itag(137)

stream_audio = yt.streams.get_by_itag(140)

stream_video.download()
