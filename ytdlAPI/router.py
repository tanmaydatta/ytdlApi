from ytdlAPI import app
from ytdlAPI.controller import index, get_video_url


app.add_url_rule('/', 'index', index)
app.add_url_rule('/<video_id>/', 'video', get_video_url)
