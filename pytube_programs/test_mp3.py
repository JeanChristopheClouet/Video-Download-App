import pytube
import os

link='https://www.youtube.com/watch?v=zVgKnfN9i34'

yt = pytube.YouTube(link)
vid = yt.streams.filter(only_audio=True).first()
output_file = vid.download()
base,ext=os.path.splitext(output_file)
new_file = base+'.mp3'
os.rename(output_file, new_file)
# except:
#     print('Donwload was not succesful')