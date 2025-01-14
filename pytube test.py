#from pytube import YouTube
from pytube import Channel

'''
video = YouTube("https://www.youtube.com/watch?v=kyXTmYZrwyo")
print("Video_title = " + video.title)
print("Video_author = " + video.author)
print("Video_length = " + str(video.length))
'''

#print(video.streams)
#download audio
'''
audio_stream = video.streams.filter(only_audio=True).first()
title = video.title
new_title = title.replace(':','-')
filename = f'{new_title}.mp3'
audio_stream.download(filename=filename)
print("done!")
'''
#try obama foundation
channel = Channel("https://www.youtube.com/c/ObamaFoundation/videos")
for url in channel.video_urls[:3]:
    print(url)


'''video_urls = []
video_urls = channel.video_urls
print(video_urls[0])

videos = []
videos = channel.videos
print(videos[0].title)
print(videos[0].length)'''