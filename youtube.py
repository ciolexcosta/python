from pytube import YouTube
YouTube('https://youtube.com/shorts/3hXdQIMCR2I').streams.get_highest_resolution().download()

https://youtube.com/shorts/3hXdQIMCR2I?feature=share