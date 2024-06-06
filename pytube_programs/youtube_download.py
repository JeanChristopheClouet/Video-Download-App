'''This program downloads all the videos in a playlist as mp3 files(so only the audio)'''
import pytube


# stores playlist url
playlist_url = input()

# create a Playlist object with the given url 
ma_p = pytube.Playlist(playlist_url)

# looping through the playlist's videos urls
for video_url in ma_p.video_urls():

    # creating YouTube object url and downloading it
    yt = pytube.YouTube(video_url)
    yt.streams.filter(type='mp3').get_audio_only().download()


