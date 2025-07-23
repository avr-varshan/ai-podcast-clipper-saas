from pytubefix import YouTube
from pytubefix.cli import on_progress

url1 = "https://www.youtube.com/watch?v=VSG9hY_t-rs"
url2 = "https://youtu.be/W4tqbEmplug?si=-P8o8z0ec0r2MWz_"
url = "https://youtu.be/4qykb6jKXdo?si=LjwXjPxMjgNuxAyH"


yt = YouTube(url,on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()

