import youtube_dl

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

def get_video_url(video_id):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info("https://www.youtube.com/watch?v=" + video_id, download=False)
    return res["url"]