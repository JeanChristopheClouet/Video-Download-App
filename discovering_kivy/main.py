import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget





class MyGrid(GridLayout):
    

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # main layout
        self.cols = 1
        self.inside = GridLayout()

        # inner layout
        self.inside.cols=2
        self.add_widget(self.inside)

        # text & text input widgets inside of the inner layout 
        self.inside.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=True)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name"))
        self.name = TextInput(multiline=True)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Email"))
        self.name = TextInput(multiline=True)
        self.inside.add_widget(self.name)

        # submit button
        self.submit = Button(text='submit', font_size=45)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('Pressed')




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()


# 10.29.2022 -> learn more about how to use kivy library's classes, especially for GridLayout
# 10.30.2022 -> learn about Button class and how to embed a 2nd grid layout 
# 11.1.2022 -> Learn kv language (for style) and fix a bug due to file extension:)
# 11.2.2022 -> learn about object properties and how to reference them on the python file
# 11.3.2022 -> learn about FloatLayout layout manager class, pos_hint, background and size_hint properties
