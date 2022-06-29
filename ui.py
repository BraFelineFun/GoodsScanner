from scanner import stream_scan, decode
from pyzbar import pyzbar
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import cv2
import time
import os


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ReportScreen(Screen):
    pass


class CameraScreen(Screen):
    def startScan(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        name = "IMG_{}.png".format(timestr)
        camera.export_to_png(name)#"IMG_{}.png".format(timestr))
        frame = cv2.imread(name)
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            # draw the barcode
            print(f"Обнаружен код:\n{obj}")
            #image = draw_barcode(obj, image)
            # print barcode type & data
            print("Тип:", obj.type)
            print("Данные:", obj.data)
            print()
        os.remove(name)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('stable.kv')


class MyApp(App):
  def build(self):
    #bl = BoxLayout(orientation = 'vertical')
    #bl.add_widget(Label(text ='Menu'))
    #bl.add_widget(Label(text = '_'))
    #bl.add_widget(Button(text = 'ok'))
    #return MyRoot()
    return kv


# class MyRoot(BoxLayout):
#     def __init__(self):
#         super(MyRoot, self).__init__()
#
#     def generate_number(self):
#         stream_scan()
