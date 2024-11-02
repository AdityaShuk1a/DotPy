from pytube import YouTube

link = YouTube("https://youtu.be/3E2SmJCoEg8?list=PLe4bSgoh2qPC8n4sSA2FuHm8oJjP3VYG2")

video = link.streams.get_highest_resolution()

video.download()