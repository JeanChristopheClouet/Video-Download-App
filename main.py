import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import pytube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


video = "https://youtu.be/HaGkk60kcjQ"

# setting up the gridlayout aka what the app will display
class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        # defining mp3 related vars
        self.mp3_label = Label(text='mp3 download :')
        self.mp3_textinput = TextInput(multiline=False)
        self.mp3_submit = Button(text='Submit')
        

        # adding mp3 related vars to home screen
        self.add_widget(self.mp3_label)
        self.add_widget(self.mp3_textinput)
        self.add_widget(self.mp3_submit) 


        # defining playlist related vars
        self.playlist_label = Label(text='playlist download :')
        self.playlist_textinput = TextInput(multiline=False)
        self.playlist_submit = Button(text='Submit')
        

        # adding playlist related vars to home screen
        self.add_widget(self.playlist_label)
        self.add_widget(self.playlist_textinput)
        self.add_widget(self.playlist_submit)

        
        # binding function to when the button is pressed
        self.mp3_submit.bind(on_press=self.mp3_pressed) 
        self.playlist_submit.bind(on_press=self.playlist_pressed) 

        # a verification label at the bottom of the page to know wether the vid has been downloaded or not
        self.verification = Label(text='', color='yellow')
        self.add_widget(self.verification)

    # The functions that allow vids to be downloaded onto the phone's hard drive

    def mp3_pressed(self, attribute):  
                
        print(type(self.mp3_textinput.text)) # TODO delete

    
            
        # creating YouTube object
        yt = pytube.YouTube(self.mp3_textinput.text)
            
        # set the text input to ''

        self.mp3_textinput.text=''
                
        # browse and select the stream

        vid = yt.streams.filter(only_audio=True).first()

        # download the vid

        output_file = vid.download(r'''Internal storage/Download''')

         # change the exctension

        base,ext=os.path.splitext(output_file)
        new_file = base+'.mp3'
        os.rename(output_file, new_file)
        self.verification.text=f'new file created at: {new_file}'




        # except pytube.exceptions.RegexMatchError:
        #     self.verification.text='download unsuccessful, pytube.exceptions.RegexMatchError'
        
        # else:
        #     self.verification.text='download unsuccessful'

        # TODO add the try and except clauses to the function below too.
        

    def playlist_pressed(self, attribute):  
        print(self.playlist_textinput.text) # TODO delete

        try:
            pl = pytube.Playlist(self.playlist_textinput.text) # Playlist instance containing Youtube objects

            for video in pl.videos: # iterating over the vids in the playlist
                vid = video.streams.filter(only_audio=True).first() # selecting only the first in a list of audio containing files 
                output_file = vid.download(r'''Internal storage/Download''') # downloading them
                base,ext=os.path.splitext(output_file) 
                new_file = base+'.mp3'
                os.rename(output_file, new_file) # changing the extension of the file to mp3


            self.verification.text='download successful'
        

        except:
            self.verification.text='download unsuccessful'
         


# the app class
class MyApp(App):
    def build(self):
        return MyGrid()


# running the app
if __name__ == '__main__':
    MyApp().run()


# ********************************************************************************************************************************************
# Studying Progression
# 10.17.2022 -> import pytube into file. Never been so happy to see the outpyt 'dick' in my life. PYTHON 3.10 FINALLY WORKING YEE-AH
# 10.18.2022 -> create YouTube object and print out some of its attributes
# 10.19.2022 -> find out about the various streams of a vid, and learn how to download a vid
# 10.21.2022 -> learn about working with captions, playlist, and channels, fiddle a bit, display urls
# 10.22.2022 -> learn about Search class, iterate over a Search object, read about exception handling and remember about else as last statement of try exept clause

# ********************************************************************************************************************************************
# Kivy learning 
# 10.29.2022 -> learn more about how to use kivy library's classes, especially for GridLayout
# 10.30.2022 -> learn about Button class and how to embed a 2nd grid layout 
# 11.1.2022 -> Learn kv language (for style) and fix a bug due to file extension:)
# 11.2.2022 -> learn about object properties and how to reference them on the python file
# 11.3.2022 -> learn about FloatLayout layout manager class, pos_hint, background and size_hint properties

# ********************************************************************************************************************************************
# YouTube downloader app project
# 7.11.2022 -> come up with a design, create the base of the main screen appearance with kivy
# 8.11.2022 -> learn how to download files in mp3 format, create functions for downloading yt vids to mp3 format files, bind buttons with functions
# 10.11.2022 -> make the functions work by fixing a bug,create playlist_pressed function, wrap function code into try/except clause
# 10.13.2022 -> make the functions ACTUALLY work by permetting them to access textinput variables (indentation at the same level as __init__) 
# 10.14.2022 -> find a vid explaining how to make apk file out of py and kv files
# 12.3.2022 -> fix the bug in the mp3_pressed class
# 12.4.2022 -> implement a function to download all the vids of a playlist in mp3 format.
# 12.5.2022 -> make a function that downloads all vids of a public playlist, add try and except clause to both pressed functions
# 12.7.2022 -> clean code, add some verification for the user so that he knows his download is succesful or not, organise project folders
# 12.10.2022 -> add more info about where to download vids, find out that my code is 97% working, spot the 3 lines possibly causing bugs
# 17.10.2022 -> run mano app on phone and find at which line it crashes.