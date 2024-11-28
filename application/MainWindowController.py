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


    def ClickedPlaylist(self, item):
        playlist_id = item.id
        SpotifyWebViewController().load_song('playlist', playlist_id)


    def ClickedAlbum(self, item):
        album_id = item.id
        SpotifyWebViewController().load_song('album', album_id)
        
        
    def ClickedArtist(self, item):
        album_id = item.id
        print(f"{album_id} Does nothing when clicked rn")
        # SpotifyWebViewController().load_song('album', album_id)

    # def startSpotify(self):
    #     pass
    #         # Open the webview window after the button is clicked
    #         # self.queue.put("open_spotify_application")

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

    # def listen_for_instructions(self):
    #     while True:
    #         instruction = self.queue.get()
    #         if instruction == "kill_spotify_application":
    #             self.on_spotify_kill()
    #         elif instruction == "spotify_application_webview_on":
    #             self.kill_button.show()
    #         elif instruction == "spotify_application_DOM_loaded":
    #             self.show_button.show()



# class UIManager:
#     def __init__(self):
#         self.main_window = MainWindow()

#     def create_ui(self):
#         self.main_window.setup_window()
#         self.main_window.setup_stylesheets()
#         self.main_window.setup_spotify_auth()
#         self.main_window.setup_timer()
#         self.main_window.init_main_ui()

#     def update_ui(self):
#         self.main_window.update_progress_bar()
#         self.main_window.update_track_info()

#     def refresh_ui(self):
#         self.main_window.refresh_search_results()




