import pytube
from pytube import YouTube
from pytube import Playlist
yt_vid = YouTube("https://www.youtube.com/shorts/KZQ1yc4yerk")

print(yt_vid.title)
# print(yt_vid.captions) # no captions on the vid

for stream in yt_vid.streams.filter(only_audio=True):
    print(stream)

vid = yt_vid.streams.get_by_itag(137)
# vid.download()


# --------------------------------- Experimenting with channels -----------------------------------------

# channel = Channel('https://www.youtube.com/channel/UChsB0fFGerVrvRxSPoF0NyQ')

# # displaying the channel vids:
# # print(channel.videos)

# # ...their urls
# print(channel.videos_url)

# --------------------------------- Experimenting with search functionality -----------------------------------------

# r = pytube.Search('naruto opening 16 kana boon')

# for result in r.results:
#     print(result.title)



# Studying Progression
# 10.17.2022 -> import pytube into file. Never been so easy to see the outpyt 'dick' in my life. PYTHON 3.10 FINALLY WORKING YEE-AH
# 10.18.2022 -> create YouTube object and print out some of its attributes
# 10.19.2022 -> find out about the various streams of a vid, and learn how to download a vid
# 10.21.2022 -> learn about working with captions, playlist, and channels, fiddle a bit, display urls
# 10.22.2022 -> learn about Search class, iterate over a Search object, read about exception handling and remember about else as last statement of try exept clause