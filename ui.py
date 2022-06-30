from kivymd.theming import ThemeManager
from scanner import stream_scan, decode

from pyzbar import pyzbar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp

import cv2
import time
import os



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


class MyApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file('ui_main.kv')

