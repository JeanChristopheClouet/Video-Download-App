import pytube

import os

yt = pytube.YouTube('https://www.youtube.com/watch?v=M5Y6t9tmBIQ')
vid = yt.streams.filter(only_audio=True).first()
output_file = vid.download(output_path=r'''C:\Users\jceyl\Videos''')
quit()
print(f"output file : {output_file}")

base,ext=os.path.splitext(output_file)
new_file = base+'.mp3'
os.rename(output_file, new_file)