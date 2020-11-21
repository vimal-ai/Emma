# import kivy module 
import kivy

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App

# it is to import Builder 
from kivy.lang import Builder

# this restrict the kivy version i.e 
# below this kivy version you cannot use the app or software 
# not coumpulsary to write it 
kivy.require('1.9.1')

# building kv file as string 
kvfile = Builder.load_string(""" 
Label: 
    text: 
        ('[b]Hello[/b] [color = ff0099]World[/color]\\n' 
        '[color = ff0099]Hello[/color] [b]World[/b]\\n' 
        '[b]Hello[/b] [color = ff0099]World:):)[/color]') 
    markup: True 
    font_size: '64pt' 
""")


# define the App class
# and just pass rest write on kvfile 
# not necessary to pass 
# can also define function in it 
class kvfileApp(App):
    def build(self):
        return kvfile


kv = kvfileApp()
kv.run() 