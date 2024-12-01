from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from WidgetDefinitions import *

# from UIElementFinder import *
from applicationTypes import *


def find_Objectss(window: QMainWindow, widgetsToFind: list[QObject]):
    found_window_objs = []
    for obj in widgetsToFind:
        obj_found = window.findChildren(obj)
        found_window_objs.extend(obj_found)
    
    return found_window_objs

def find_aanObject(window: QMainWindow, widgetToFind: QObject):
    found_window_objs = window.findChildren(widgetToFind)
    return found_window_objs



class UIUpdateLogic():
    def __init__(self, window: QMainWindow):
        self.window = window
        
    def updateUIOnTrackClick(self, item: TrackItem):
        # [TrackArtrwork, TrackTitle, TrackArtist, TrackID, TrackDuration, TrackPopularity, PlayButn]
        found_objs = find_Objectss(self.window, [TrackArtworkWidget, TrackTitle, TrackArtist, TrackID, TrackDuration, TrackPopularity, PlayButtn])
        
        for obj in found_objs:
            print(obj)
            if isinstance(obj, TrackArtworkWidget):
                obj.setImage(item.cover_url)
                
            elif isinstance(obj, TrackTitle):
                obj.setText(item.name)
            
            elif isinstance(obj, TrackArtist):
                obj.setText(item.artist)
            
            elif isinstance(obj, TrackID):
                obj.setText(item.id)
                
            elif isinstance(obj, TrackDuration):
                obj.setText(str(item.duration))
                
            elif isinstance(obj, TrackPopularity):
                obj.setText(str(item.popularity))
                
            elif isinstance(obj, PlayButtn):
                obj.set_as_playing()
        
        
        # found_objs[0].setImage(item.cover_url)
        # found_objs[1].setText(item.name)
        # found_objs[2].set_as_playing()
        
        
    def set_plybtn_as_playing(self):
        found_objs = find_aanObject(self.window, TrackProgressWidget)
        for obj in found_objs:
            obj.play()
        
    def set_plybtn_as_paused(self):
        found_objs = find_aanObject(self.window, TrackProgressWidget)
        for obj in found_objs:
            obj.pause()