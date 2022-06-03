from scanner import stream_scan
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



class MyApp(App):
  def build(self):
    #bl = BoxLayout(orientation = 'vertical')
    #bl.add_widget(Label(text ='Menu'))
    #bl.add_widget(Label(text = '_'))
    #bl.add_widget(Button(text = 'ok'))
    return MyRoot()

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def generate_number(self):
        stream_scan()
