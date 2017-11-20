import youtube_dl
from flask_cors import cross_origin

ydl_opts = {
         'format': 'best',
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
             'preferredquality': '192',
        }],
    }

def index():
    return '<h1>It works!</h1>'

@cross_origin()
def get_video_url(video_id):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info("https://www.youtube.com/watch?v=" + video_id, download=False)
    return res["url"]