from scanner import stream_scan, decode
from pyzbar import pyzbar
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
import cv2
import time
import os

Window.clearcolor = (208/255.0, 208/255.0, 208/255.0, 1)

class WelcomeScreen(Screen):
    pass


# class SecondScreen(Screen):
#     pass


class ReportScreen(Screen):
    pass


class ScanScreen(Screen):
    def startScan(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        name = "IMG_{}.png".format(timestr)
        camera.export_to_png(name)  # "IMG_{}.png".format(timestr))
        frame = cv2.imread(name)
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            print(f"Обнаружен код:\n{obj}")
            # image = draw_barcode(obj, image)
            # print barcode type & data
            print("Тип:", obj.type)
            print("Данные:", obj.data)
            print()
        os.remove(name)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('ui_main.kv')


class MyApp(App):
    def build(self):
        return kv

# class MyRoot(BoxLayout):
#     def __init__(self):
#         super(MyRoot, self).__init__()
#
#     def generate_number(self):
#         stream_scan()
