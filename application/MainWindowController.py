import os
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from queue import Queue
import webview
import webview.menu as wm
import webview.window
from threading import Thread
import threading
import time
import re
from enum import Enum
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QLabel, QListWidget,QProgressBar
from PyQt5.QtWidgets import QListView, QListWidgetItem, QMessageBox, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QProgressBar
from PyQt5.QtCore import Qt, pyqtSlot
import threading
from queue import Queue
import spotipy
from spotipy.oauth2 import SpotifyOAuth


from SpotifyWebViewController import *
from SearchManager import *


# start QT application
# start WebView of spotify 
"""
Could be called MainWindowUIEventsController
more like a WidgetDefintion to Webview Middle man

"""


"""
This could be like a general class for all the UI elements to access other UI elements
This acts as my pub sub kinda
    because UI elements know of eachother exsistance(defintions) and can find them on the pyqt5 window
    with the find object functions below
"""

def find_Objects(window: QMainWindow, widgetsToFind: list[QObject]):
    found_window_objs = []
    for obj in widgetsToFind:
        obj_found = window.findChild(obj)
        found_window_objs.append(obj_found)
    
    return found_window_objs

def find_anObject(window: QMainWindow, widgetToFind: QObject):
    found_window_objs = window.findChild(widgetToFind)
    return found_window_objs


class MainWindowController():
    def __init__(self, window: QMainWindow = None):
        self.window = window
    
    """
    More of a PYQT UI feature for formating rather than a action taken on the WebView  
    """
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.userControlsWidget.setMinimumWidth(int(self.mainContentWidget.width() * 0.5))
        # self.artwork_placeholder.setMinimumHeight(int(self.userControlsWidget.height() * 0.20))
        # self.artwork_placeholder.setMinimumWidth(int(self.userControlsWidget.height() * 0.20))
        self.userBtnControlsWidget.setMinimumHeight(int(self.userControlsWidget.height() * 0.60))

    def RunSearch(self, query: str):
        from WidgetDefinitions import SearchTextWidget, TrackTabel, AlbumsTabel, ArtistsTabel, PlaylistsTabel

        objects_to_update = [SearchTextWidget, TrackTabel, AlbumsTabel, ArtistsTabel, PlaylistsTabel]
        found_window_objs = find_Objects(self.window, objects_to_update)
        print(len(found_window_objs))
        
        SearchManager().perform_search(query, found_window_objs)
    
    """
    This should be a function within playButton widget?
    """
    def ClickedPlay(self):
        SpotifyWebViewController().click_play_btn()


    def ClickedNextTrack(self):
        SpotifyWebViewController().click_next_track_btn()
        
    
    def ClickedPrevTrack(self):
        SpotifyWebViewController().click_prev_track_btn()
        

    def ClickedTrack(self, item):
        from WidgetDefinitions import TrackArtworkWidget, TrackTitle, PlayButtn

        track_id = item.id
        SpotifyWebViewController().load_song('track', track_id)
        
        found_objs = find_Objects(self.window, [TrackArtworkWidget, TrackTitle, PlayButtn])
        found_objs[0].setImage(item.cover_url)
        found_objs[1].setText(item.name)
        found_objs[2].set_as_playing()
        
        self.ClickedPlay()
        


    def ClickedPlaylist(self, playlist_item):
        from WidgetDefinitions import PlaylistQueueLabel, PlaylistQueueTabel
        playlist_id = playlist_item.id
        SpotifyWebViewController().load_song('playlist', playlist_id)
        
        found_objs = find_Objects(self.window, [PlaylistQueueLabel, PlaylistQueueTabel])
        SearchManager().perform_queue_loading(playlist_item, found_objs)
        # Programmatically click an item
        item_index = 1  # Index of the item you want to click (0-based)
        found_objs[1].itemClicked.emit(found_objs[1].item(item_index))
        
        """
        Once queue table is loaded
        - Maybe switch tabs
        - maybe play first song
        - maybe play random song?
        """
        



    def ClickedAlbum(self, item):
        album_id = item.id
        SpotifyWebViewController().load_song('album', album_id)
        
        
    def ClickedArtist(self, item):
        album_id = item.id
        print(f"{album_id} Does nothing when clicked rn")
        # SpotifyWebViewController().load_song('album', album_id)

    def get_song_progress(self):
        value = SpotifyWebViewController().track_progress()
        return value
    
    
    
    def destroy_spotify_webview(self):
        # show the window for a few seconds before destroying it:
        # time.sleep(5)
        # Check if there are any windows before proceeding
        if len(webview.windows) > 0:
            print('Destroying window..')
            webview.windows[0].destroy()  # Destroy the first window
            print('Destroyed!')
        else:
            print("Window already Destoryed.")






