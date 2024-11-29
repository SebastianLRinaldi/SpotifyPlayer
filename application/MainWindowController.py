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
# from WidgetDefinitions import *


# start QT application
# start WebView of spotify 
"""
Could be called MainWindowUIEventsController
more like a WidgetDefintion to Webview Middle man

"""
class MainWindowController():
    def __init__(self):
        pass
    
    """
    More of a PYQT UI feature for formating rather than a action taken on the WebView  
    """
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.userControlsWidget.setMinimumWidth(int(self.mainContentWidget.width() * 0.5))
        # self.artwork_placeholder.setMinimumHeight(int(self.userControlsWidget.height() * 0.20))
        # self.artwork_placeholder.setMinimumWidth(int(self.userControlsWidget.height() * 0.20))
        self.userBtnControlsWidget.setMinimumHeight(int(self.userControlsWidget.height() * 0.60))

    def RunSearch(self, query: str, objects_to_update: List[QObject]):
        SearchManager().perform_search(query, objects_to_update)
    
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
        track_id = item.id
        SpotifyWebViewController().load_song('track', track_id)
        self.ClickedPlay()
        


    def ClickedPlaylist(self, playlist_item, objects_to_update: List[QObject]):
        playlist_id = playlist_item.id
        SpotifyWebViewController().load_song('playlist', playlist_id)
        SearchManager().perform_queue_loading(playlist_item, objects_to_update)
        # Programmatically click an item
        item_index = 1  # Index of the item you want to click (0-based)
        objects_to_update[1].itemClicked.emit(objects_to_update[1].item(item_index))
        
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






