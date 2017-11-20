from ytdlAPI import app
from ytdlAPI.controller import index


app.add_url_rule('/', 'index', index)
