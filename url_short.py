import pyshorteners

url="https://www.youtube.com/watch?v=OKQhS3Zvw9s&list=PLk6c4eFKmugRtioVfxAsqHqsTs637BgWD"

print("short url : \n" +str(pyshorteners.Shortener().tinyurl.short(url)))