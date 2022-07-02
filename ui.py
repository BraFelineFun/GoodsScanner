from pyzbar import pyzbar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy import platform
from DataMTRX import datamatrix
from kivy_garden import xcamera
import cv2
import time
import os


dataBase = {"b'5055856412670'": "Тип Штрих кода: EAN13\nСтрана производитель: Великобритания\nИгровой диск Dishonored 2",
            "b'0711719843948'": "Тип Штрих кода: EAN13\nСтрана производитель: США или Канада\nИгровой диск BloodBorne"}


class WelcomeScreen(Screen):
    pass


class ReportScreen(Screen):
    pass


class ScanScreen(Screen):
    def showData(self, obj):
        value = dataBase.get(str(obj))
        if value is not None:
            dialog = MDDialog(text = str(value))
            dialog.open()
        else:
            dialog = MDDialog(text=str(obj))
            dialog.open()

    def startScan(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        name = "IMG_{}.png".format(timestr)
        camera.export_to_png(name)  # "IMG_{}.png".format(timestr))
        if(platform == "android"):
            frame = cv2.imread("/data/data/org.test.contafactapp/files/{}".format(name))
        else:
            frame = cv2.imread(name)
        data = ""
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            print(f"Обнаружен код:\n{obj}")
            # image = draw_barcode(obj, image)
            # print barcode type & data
            print("Тип:", obj.type)
            print("Данные:", obj.data)
            data = obj.data
            print()
        if(platform == "android"):
            os.remove("/data/data/org.test.contafactapp/files/{}".format(name))
        else:
            os.remove(name)

        if data != "":
            self.showData(str(data))

    def doScanMatrix(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        name = "IMG_{}.png".format(timestr)
        camera.export_to_png(name)  # "IMG_{}.png".format(timestr))
        if platform =="android":
            data = datamatrix("/data/data/org.test.contafactapp/files/{}".format(name))
        else:
            data = datamatrix(name)
        self.showData((str(data)))
        if (platform == "android"):
            os.remove("/data/data/org.test.contafactapp/files/{}".format(name))
        else:
            os.remove(name)


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)


    def waitRequest(self):
        from android.permissions import request_permissions, Permission
        request_permissions(
            [Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        if platform == "android":
            self.waitRequest()
        self.root = Builder.load_file('ui_main.kv')
        # if platform == "android":
        #     from android.permissions import request_permissions, Permission
        #     request_permissions([Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

