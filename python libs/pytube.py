from pytube import YouTube

link = YouTube("bas link dalna idhar baaki ho jaega")

video = link.streams.get_highest_resolution()

video.download()