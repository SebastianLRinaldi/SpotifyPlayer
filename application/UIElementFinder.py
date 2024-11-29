from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 


"""
Will find all objects then will get if its a instance of something and do it on that
"""



class UIElementFinder():
    def __init__(self, window: QMainWindow):
        self.window = window
        pass
    
    def find_Objects(self, widgetsToFind: list[QObject]):
        found_window_objs = []
        for obj in widgetsToFind:
            obj_found = self.window.findChild(QObject, obj)
            found_window_objs.append(obj_found)
        
        return found_window_objs

    def find_anObject(self, widgetNameToFind: str):
        found_window_objs = self.window.findChild(QObject, widgetNameToFind)
        return found_window_objs
    
