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
from typing import List


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



"""
Might need to make a contianer class
as well as a widget class per object I want to make
"""
class WindowStyle:
    def setup_stylesheets(self):
        # self.setStyleSheet("background-color: white;")
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-family: 'Roboto', sans-serif;
            }
            QLabel {
                font-weight: bold;
            }
            QLineEdit {
                background-color: #2c2c3b;
                color: white;
                border: 1px solid #3a3a4a;
                border-radius: 20px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3a3a4a;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px;
                font-size: 14px;
                font-family: 'Roboto', sans-serif;
            }
            QPushButton:hover {
                background-color: #454d5b;
            }
            QProgressBar {
                text-align: center;
                background-color: #2c2c3b;
                border: 1px solid #3a3a4a;
                border-radius: 10px;
                height: 8px;
                font-size: 12px;
            }
            QProgressBar::chunk {
                background-color: purple;
                border-radius: 5px;
            }
        """)





class Button(QPushButton):
    def __init__(self, text="Click me!", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol

# class BaseContainerWidget(QWidget):
#     def __init__(self, text="Click me!"):
#         super().__init__(text)
        
#     def init_main_ui(self):
#         """
#         https://www.pythonguis.com/tutorials/pyqt-layouts/
#         """
#         self.mainContainer = QGridLayout()
#         self.mainContentWidget = QWidget()
#         self.mainContentWidget.setLayout(self.mainContainer)

#         self.userControlsContainer = QGridLayout()
#         self.userControlsWidget = QWidget()
#         self.userControlsWidget.setLayout(self.userControlsContainer)
#         self.userControlsWidget.setStyleSheet("border: 1px solid white; border-radius: 15px;")

#         # adds mainContentWidget to QMainWindow
#         self.setCentralWidget(self.mainContentWidget) 
#         # adds player controls to the mainContentContainer
        
#         # self.userControlsWidget.setMinimumHeight(int(self.mainContentWidget.height() * 1))
#         self.mainContainer.addWidget(self.userControlsWidget, 0, 2, 6, 1)
#         self.userControlsWidget.setMaximumWidth(int(self.mainContentWidget.width() * 0.5))
#         # self.configure_main_interface()
#         self.show()
        

# class UserControlWidget(QWidget):
#     def __init__(self, text="Click me!"):
#         super().__init__(text)
    
#     def userControls(self):
#         """ This could be its own top bar"""
#         self.top_bar_container = QHBoxLayout()
#         self.top_bar = QWidget()
#         self.top_bar.setLayout(self.top_bar_container)
#         self.title_label = QLabel("Spotify")
#         self.title_label.setStyleSheet("""
#                                        font-size: 35px; 
#                                        font-weight: bold; 
#                                        background-color: #2c2c3b;
#                                        """)
#         self.top_bar_container.addWidget(self.title_label)
#         self.userControlsContainer.addWidget(self.top_bar, 0, 0, 1, 2, Qt.AlignCenter)

#         self.trackInfoPanel(1, 0, 1, 2)
#         self.trackControls(2, 0, 1, 2)



class TrackTitle(QLabel):
    def __init__(self, text="No track selected", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol


# class TrackInfoWidget(QWidget):
    
#     def __init__(self, text="Click me!"):
#         super().__init__(text)
        
        
#     def trackInfoPanel(self, row: int, column: int, rowSpan: int, columnSpan: int):
#         self.trackInfoPanelContainer = QGridLayout()
#         self.trackInfoPanelWidget = QWidget()
#         self.trackInfoPanelWidget.setLayout(self.trackInfoPanelContainer)

#         self.trackArtworkDisplay()

#         # self.track_info = QLabel("No track selected")
#         # self.trackInfoPanelContainer.addWidget(self.track_info, 0, 2, 1, 2, Qt.AlignCenter)

#         self.trackProgress()

#         self.userControlsContainer.addWidget(self.trackInfoPanelWidget, row, column, rowSpan, columnSpan)

from TimingManager import *
"""
Everything that uses this controlor should be in its own class?
so we can make one instance on creating the pyqt5 applcation 
instead of creating it every time we need to do something
"""
from MainWindowController import *
   
class TrackProgressWidget(QProgressBar):
    
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.setRange(0, 100)
        self.setAlignment(Qt.AlignCenter)
        # self.loading_bar.setOrientation(QtCore.Qt.Vertical)
        self.setFormat(f"remaing: %p%")
        self.setValue(0)
        self.mwc = MainWindowController()
        
        
        # Timer to update the progress
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Update every 1 second
        self.timer.timeout.connect(self.update_progress)
        
        # Simulated progress value
        self.progress = 0

        # # Start the timer
        # self.timer.start()

    def update_progress(self):
        """Update the progress bar's value"""
        value = self.mwc.get_song_progress()
        self.setValue(value)
        print(f"Progress: {value}%")
        
        
    def play(self):
        """Start the progress timer."""
        self.timer.start()  # Start the timer when playing the song
            
    def pause(self):
        """stop the progress timer."""
        self.timer.stop()  # Stop the timer when the song is paused
            
    def reset(self):
        """
        Reset the progress
        - stop the timer
        - playbutton to set to show "Play" on the button.
        
        Reset should happen when going to next or prev or exiting or new song selected - yes
        If we need to reset when a new song is selected then all tables will need to search for this element
        The tables need to be able to access the elements anyways becauase they have to also set the 
            images in other elements like the artist and song cover when a item is clicked
        """
        self.progress = 0
        self.setValue(self.progress)
        self.timer.stop()  # Stop the timer when resetting the song
        
    # def trackProgress(self):
    #     self.loading_bar = QProgressBar()
    #     self.loading_bar.setRange(0, 100)
    #     self.loading_bar.setAlignment(Qt.AlignCenter)
    #     # self.loading_bar.setOrientation(QtCore.Qt.Vertical)
    #     self.loading_bar.setFormat(f"remaing: %p%")
    #     self.loading_bar.setValue(0)
    #     self.trackInfoPanelContainer.addWidget(self.loading_bar, 1, 1, 1, 3)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class TrackArtworkWidget(QLabel): 
    def __init__(self, text="Click me!", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        

        self.setFixedSize(200, 200)

        self.setStyleSheet(f"""
            QLabel {{
                background-color: #2c2c3b;
                border-radius: {100}px;
            }}
        """)

        self.setText(f"{self.height(), self.width()}")
        
        
        """
        need to add functions similar to the ProgressBar 
        where other elements can set and change the content of the artwork widget
        so will need a replace artwork function that sets new artwork to this widget
        
        maybe set Background color to avg color or icon? 
        """
    def setImage(self, url: str):
        self.load_image(url)
        
        
        # pixmap = QPixmap()
        # # if pixmap.load(url):
        # if pixmap.loadFromData(url.encode()):
        #     print(f"FLoaded image from URL: {url}")
        #     self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        # else:
        #     print(f"Failed to load image from URL: {url}")


    def load_image(self, url):
        manager = QNetworkAccessManager(self)
        manager.finished.connect(self.handle_image_loaded)
        request = QNetworkRequest(QUrl(url))
        manager.get(request)
        
    def handle_image_loaded(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            image_data = reply.readAll()
            image = QImage()
            
            if image.loadFromData(image_data):
                # pixmap = QPixmap.fromImage(image) #.scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                # self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio))
                self.setPixmap(QPixmap.fromImage(image).scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                print(self.size())
            else:
                print("Error loading image")
        else:
            print("Network error:", reply.errorString())





        # self.trackInfoPanelContainer.addWidget(self.artwork_placeholder, 0, 0, 2, 2)
        # self.artwork_placeholder.setMaximumHeight(int(self.userControlsWidget.height() * 0.25))
        # self.artwork_placeholder.setMaximumWidth(int(self.userControlsWidget.width() * 0.25))

# class TrackControlWidget(QWidget):
#     def __init__(self, text="Click me!"):
#         super().__init__(text)
        
#     def trackControls(self, row: int, column: int, rowSpan: int, columnSpan: int):

#         self.userBtnControlsContainer = QGridLayout()
#         self.userBtnControlsWidget = QWidget()
#         self.userBtnControlsWidget.setLayout(self.userBtnControlsContainer)

#         # self.button = QPushButton("Find Elm")
#         # self.button.clicked.connect(start_spotify.mark_custom_elements)
#         # self.userBtnControlsContainer.addWidget(self.button, 0, 0, 1, 2)

class PlayButtn(QPushButton):
    def __init__(self, window: QMainWindow, text="PLAY", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        # self.play_btn = QPushButton("PLAY")
        # self.play_btn.clicked.connect(self.start_shadow_controls)
        # self.userBtnControlsContainer.addWidget(self.play_btn, 1, 0, 1, 2)
        # self.play_btn.setMaximumHeight(int(self.userBtnControlsWidget.height() * 0.65))
        self.is_playing = False
        self.window = window
        self.clicked.connect(lambda: self.on_item_clicked())

     
    def on_item_clicked(self):
        MainWindowController().ClickedPlay()
        self.update_playbtn_state()
        
    def set_as_playing(self):
        found_window_objs = find_anObject(self.window, TrackProgressWidget)
        self.is_playing = True
        self.setText("PAUSE")
        found_window_objs.play()
        
    def set_as_paused(self):
        found_window_objs = find_anObject(self.window, TrackProgressWidget)
        self.is_playing = False
        self.setText("PLAY")
        found_window_objs.pause()
    
    def update_playbtn_state(self):
        
        """
        if self.is_playing is True: when clicked
            pause the song
            tell user this button will play the song 
            when clicked next
            
        if self.is_playing is False: when clicked
            play the song
            tell user this button will pause the song 
            when clicked next
        """
        if self.is_playing:
            self.set_as_paused()
        else:
            self.set_as_playing()
            
class NextTrackButtn(QPushButton):
    def __init__(self, text="NEXT", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.clicked.connect(lambda:MainWindowController().ClickedNextTrack())
        # self.next_btn = QPushButton("NEXT")
        # self.userBtnControlsContainer.addWidget(self.next_btn, 2, 1,1,1)
        # self.next_btn.setMaximumHeight(int(self.userBtnControlsWidget.height() * 0.50))

class PrevousTrackButtn(QPushButton):
    def __init__(self, text="PREV", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.clicked.connect(lambda:MainWindowController().ClickedPrevTrack())
        # self.prev_btn = QPushButton("PREV")
        # self.userBtnControlsContainer.addWidget(self.prev_btn, 2, 0,1,1)
        # self.prev_btn.setMaximumHeight(int(self.userBtnControlsWidget.height() * 0.50))







        
class SearchBarWidget(QLineEdit):
    def __init__(self, window: QMainWindow, text="Search...", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.window = window
        self.returnPressed.connect(lambda: self.find_update_objects_and_search())

     
    def find_update_objects_and_search(self):
        objList = [SearchTextWidget, TrackTabel, AlbumsTabel, ArtistsTabel, PlaylistsTabel]
        found_window_objs = find_Objects(self.window, objList)
        MainWindowController().RunSearch(self.text(), found_window_objs)
        

 

        
        # return searchTextWidget
    
        
        
    # def searchBar(self):
    #     self.search_input = QLineEdit()
    #     self.search_input.setPlaceholderText("Search...")
    #     self.search_input.returnPressed.connect(self.perform_search)
    #     self.mainContainer.addWidget(self.search_input, 0, 0, 1, 2)

class SearchTextWidget(QLabel):
    def __init__(self, text="Result will appear here", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        # self.result_label = QLabel("Result will appear here")
        # self.mainContainer.addWidget(self.result_label, 1, 0)
        
        
        
        
        


        
# class SuperItems():
class TrackTableLabel(QLabel):
    def __init__(self, text="track_label", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
class TrackTabel(QListWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.window = window #"""Check if we can just do self.window"""

        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item: TrackItem):
        print(f"TrackObject: {item}")
        MainWindowController().ClickedTrack(item)
        
        found_objs = find_Objects(self.window, [TrackArtworkWidget, TrackTitle, PlayButtn])
        found_objs[0].setImage(item.cover_url)
        found_objs[1].setText(item.name)
        found_objs[2].set_as_playing()


class AlbumsTableLabel(QLabel):
    def __init__(self, text="album_label", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
class AlbumsTabel(QListWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        # self.albumlist_widget = QListWidget()
        # self.albumlist_widget.itemClicked.connect(self.ClickedAlbum)
        
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        print(f"AlbumObject: {item}")
        MainWindowController().ClickedAlbum(item)


class ArtistsTableLabel(QLabel):
    def __init__(self, text="artists_label", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol

class ArtistsTabel(QListWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        # self.artistslist_widget = QListWidget()
        # self.artistslist_widget.itemClicked.connect(self.Clicked)
        
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        print(f"ArtistObject: {item}")
        MainWindowController().ClickedArtist(item)




class PlaylistsTableLabel(QLabel):
    def __init__(self, text="playlist_label", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
class PlaylistsTabel(QListWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.window = window
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, playlist_item):
        print(f"PlaylistObject: {playlist_item}")
        found_objs = find_Objects(self.window, [PlaylistQueueLabel, PlaylistQueueTabel])
        # found_objs[0].setImage(item.cover_url)
        # found_objs[1].setText(item.name)
        MainWindowController().ClickedPlaylist(playlist_item, found_objs)



class PlaylistQueueLabel(QLabel):
    def __init__(self, text="current_playlist_title", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
class PlaylistQueueTabel(QListWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        self.window = window
        
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        print(f"TrackObject: {item}")
        MainWindowController().ClickedTrack(item)
        
        found_objs = find_Objects(self.window, [TrackArtworkWidget, TrackTitle, PlayButtn])
        found_objs[0].setImage(item.cover_url)
        found_objs[1].setText(item.name)
        found_objs[2].set_as_playing()

