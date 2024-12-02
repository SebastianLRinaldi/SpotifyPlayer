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
from datetime import timedelta

from TimingManager import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply


"""
This could be like a general class for all the UI elements to access other UI elements
This acts as my pub sub kinda
    because UI elements know of eachother exsistance(defintions) and can find them on the pyqt5 window
    with the find object functions below
"""

# def find_Objects(window: QMainWindow, widgetsToFind: list[QObject]):
#     found_window_objs = []
#     for obj in widgetsToFind:
#         obj_found = window.findChild(obj)
#         found_window_objs.append(obj_found)
    
#     return found_window_objs

# def find_anObject(window: QMainWindow, widgetToFind: QObject):
#     found_window_objs = window.findChild(widgetToFind)
#     return found_window_objs


# """
# Might need to make a contianer class
# as well as a widget class per object I want to make
# """
# class WindowStyle:
#     def setup_stylesheets(self: QWidget):
#         # self.setStyleSheet("background-color: white;")
#         self.setStyleSheet("""
#             QWidget {
#                 background-color: #1e1e2f;
#                 color: white;
#                 font-family: 'Roboto', sans-serif;
#             }
#             QListWidget::item:selected {
#                 background-color: #D8BFD8;
#                 color: white;
#             }
#             QListWidget::item {
#                 background-color: white;
#             }
#             QLabel {
#                 font-weight: bold;
#             }
#             QLineEdit {
#                 background-color: #2c2c3b;
#                 color: white;
#                 border: 1px solid #3a3a4a;
#                 border-radius: 20px;
#                 padding: 10px;
#                 font-size: 14px;
#             }
#             QPushButton {
#                 background-color: #3a3a4a;
#                 color: white;
#                 border: none;
#                 border-radius: 20px;
#                 padding: 10px;
#                 font-size: 14px;
#                 font-family: 'Roboto', sans-serif;
#             }
#             QPushButton:hover {
#                 background-color: #454d5b;
#             }
#             QProgressBar {
#                 text-align: center;
#                 background-color: #2c2c3b;
#                 border: 1px solid #3a3a4a;
#                 border-radius: 10px;
#                 height: 8px;
#                 font-size: 12px;
#             }
#             QProgressBar::chunk {
#                 background-color: purple;
#                 border-radius: 5px;
#             }
#         """)



class ConnectedWidget(QWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1, *args, **kwargs):
        """
        Base class for widgets that initializes common properties like ui_handler,
        widgetRow, and widgetCol.
        
        :param ui_handler: The UI handler instance.
        :param widgetRow: Row index for the widget (default -1).
        :param widgetCol: Column index for the widget (default -1).
        :param *args: Additional arguments for the widget.
        :param **kwargs: Additional keyword arguments for the widget.
        """
        super().__init__(*args, **kwargs)
        self.ui_handler = ui_handler
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol

        
        
class IsolatedWidget(QWidget):
    def __init__(self, widgetRow=-1, widgetCol=-1, *args, **kwargs):
        """
        Base class for widgets that do not control or update other elements in the UI.

        :param widgetRow: Row index for the widget (default -1).
        :param widgetCol: Column index for the widget (default -1).
        :param *args: Additional arguments for the widget.
        :param **kwargs: Additional keyword arguments for the widget.
        """
        super().__init__(*args, **kwargs)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        # No UI control logic here, this widget is Isolated.
 
        
        



class Button(QPushButton):
    def __init__(self, text="Click me!", widgetRow = -1, widgetCol = -1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol

# class TrackTitle(QLabel):
#     def __init__(self, text="No track selected", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol
#         self.setObjectName("TrackTitle")
        
# class TrackArtist(QLabel):
#     def __init__(self, text="No artist for track", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol
        
# class TrackID(QLabel):
#     def __init__(self, text="No id for track", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol
        
        
# class TrackDuration(QLabel):
#     def __init__(self, text="No duration in ms for track", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol


# class TrackPopularity(QLabel):
#     def __init__(self, text="No populatirt for track", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol


class TrackTitle(QLabel, IsolatedWidget):
    def __init__(self, text="No track selected", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)


class TrackArtist(QLabel, IsolatedWidget):
    def __init__(self, text="No artist for track", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)


class TrackID(QLabel, IsolatedWidget):
    def __init__(self, text="No id for track", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)


class TrackDuration(QLabel, IsolatedWidget):
    def __init__(self, text="No duration in ms for track", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)
        

class TrackRunningDuration(QLabel, ConnectedWidget):
    def __init__(self, text="No duration in ms for track", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)


class TrackPopularity(QLabel, IsolatedWidget):
    def __init__(self, text="No popularity for track", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow, widgetCol)
        self.setText(text)
        


"""
Everything that uses this controlor should be in its own class?
so we can make one instance on creating the pyqt5 applcation 
instead of creating it every time we need to do something
"""
# class TrackArtworkWidget(QLabel): 
#     def __init__(self, text="Click me!", widgetRow = -1, widgetCol = -1):
#         super().__init__(text)
#         self.widgetRow = widgetRow
#         self.widgetCol = widgetCol

#         self.setFixedSize(200, 200)

#         self.setStyleSheet(f"""
#             QLabel {{
#                 background-color: #2c2c3b;
#                 border-radius: {100}px;
#             }}
#         """)

#         self.setText(f"{self.height(), self.width()}")
        
        
#         """
#         need to add functions similar to the ProgressBar 
#         where other elements can set and change the content of the artwork widget
#         so will need a replace artwork function that sets new artwork to this widget
        
#         maybe set Background color to avg color or icon? 
#         """
#     def setImage(self, url: str):
#         self.load_image(url)
        
        
#         # pixmap = QPixmap()
#         # # if pixmap.load(url):
#         # if pixmap.loadFromData(url.encode()):
#         #     print(f"FLoaded image from URL: {url}")
#         #     self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio))
#         # else:
#         #     print(f"Failed to load image from URL: {url}")


#     def load_image(self, url):
#         manager = QNetworkAccessManager(self)
#         manager.finished.connect(self.handle_image_loaded)
#         request = QNetworkRequest(QUrl(url))
#         manager.get(request)
        
#     def handle_image_loaded(self, reply: QNetworkReply):
#         if reply.error() == QNetworkReply.NetworkError.NoError:
#             image_data = reply.readAll()
#             image = QImage()
            
#             if image.loadFromData(image_data):
#                 # pixmap = QPixmap.fromImage(image) #.scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
#                 # self.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio))
#                 self.setPixmap(QPixmap.fromImage(image).scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
#                 print(self.size())
#             else:
#                 print("Error loading image")
#         else:
#             print("Network error:", reply.errorString())


class TrackArtworkWidget(QLabel, IsolatedWidget):
    def __init__(self, text="Click me!", widgetRow=-1, widgetCol=-1):
        # Initialize IsolatedWidget with row and column info
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
    
        # Fixed size for the artwork widget
        self.setFixedSize(200, 200)

        # Style for the widget (circular background)
        self.setStyleSheet(f"""
            QLabel {{
                background-color: #2c2c3b;
                border-radius: {100}px;
            }}
        """)

        # Set initial text (for testing or fallback)
        self.setText(f"{self.height()}, {self.width()}")

    def setImage(self, url: str):
        """ Set the image from the given URL. """
        self.load_image(url)

    def load_image(self, url):
        """ Load the image from the URL. """
        manager = QNetworkAccessManager(self)
        manager.finished.connect(self.handle_image_loaded)
        request = QNetworkRequest(QUrl(url))
        manager.get(request)

    def handle_image_loaded(self, reply: QNetworkReply):
        """ Handle the loaded image and update the pixmap. """
        if reply.error() == QNetworkReply.NetworkError.NoError:
            image_data = reply.readAll()
            image = QImage()
            
            if image.loadFromData(image_data):
                # Set the pixmap scaled to widget size
                pixmap = QPixmap.fromImage(image).scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.setPixmap(pixmap)
                # print(self.size())
            else:
                print("Error loading image")
        else:
            print("Network error:", reply.errorString())

class TrackProgressWidget(QProgressBar, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow = -1, widgetCol = -1):
        super().__init__(ui_handler, widgetRow, widgetCol)
        
        self.setRange(0, 100)
        self.setAlignment(Qt.AlignCenter)
        # self.loading_bar.setOrientation(QtCore.Qt.Vertical)
        self.setFormat(f"remaing: %p%")
        self.setValue(0)
        self.track_duration = ""
        self.track_running_duration = ""
    
        
        
        # Timer to update the progress
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Update every 1 second
        self.timer.timeout.connect(self.update_progress)
        
        # Simulated progress value
        self.progress = 0
        
    def set_track_duration(self, time: str):
        self.track_duration = time
        
    def set_track_running_duration(self, time: str):
        self.track_running_duration = time
        

    def update_progress(self):
        """Update the progress bar's value"""
        """
        Need to stop the timer when song reaches end either by duration or %%
        """
        value = self.ui_handler.get_track_progress()
        self.setValue(value)
        print(f"Progress: {value}%")
        
        time_value = self.ui_handler.get_running_time_progress()
        self.set_track_running_duration(time_value)
        self.ui_handler.send_track_progress()
        print(f"Time: {time_value}")
        
        self.check_if_track_is_over()
        
    def check_if_track_is_over(self):
        
        """
        If just a song no queue
            stop
        if Just a song but queue
            continue top of queue
        if playlist/album in queue
            continue top of queue
        """
        # print("Checking!")
        # print(f"{self.track_running_duration} == {self.track_duration}")


        # Check if the current duration is greater than the target time
        if self.track_running_duration in ("00:01", "00:00"):
            print(f"Duration less than {self.track_running_duration}.")
            print("STOPPING")
            
            self.ui_handler.set_track_as_not_playing()
            self.ui_handler.set_plybtn_as_paused()
            self.reset()
            
            self.ui_handler.ClickedNextTrack()
            
            
        # Check if the current duration matches any target time
        # if self.track_running_duration in target_times:

            
        
    def progress_start(self):
        """Start the progress timer."""
        self.timer.start()  # Start the timer when playing the song
            
    def progress_stop(self):
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
        # self.timer.stop()  # Stop the timer when resetting the song
        




"""
At first moving the ability to change the plybtn to the UiUpdate logic when
it can be done here is strange but when we have two or more playbtns 
we will need to update them all so this works fine
"""
class PlayButtn(QPushButton, ConnectedWidget):
    def __init__(self, ui_handler, text="PLAY", widgetRow = -1, widgetCol = -1):
        ConnectedWidget.__init__(self, ui_handler, widgetRow, widgetCol)
        QPushButton.__init__(self, text)

        self.is_playing = False

        self.clicked.connect(lambda: self.on_item_clicked())
        
    def on_item_clicked(self):
        self.ui_handler.ClickedPlay()
        self.update_playbtn_state()
        
    def set_as_playing(self):
        self.ui_handler.set_track_as_playing()
        self.ui_handler.set_plybtn_as_playing()
        
        
    def set_as_paused(self):
        self.ui_handler.set_track_as_not_playing()
        self.ui_handler.set_plybtn_as_paused()
        
        
    
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


"""
Theses just go up and down the queue
When we add shuffle it will place the currently selected song at top so you don't lose place and can contiune
to go through the queue without worring about hitting the bttom right after you shuffle
"""
class NextTrackButtn(QPushButton, ConnectedWidget):
    def __init__(self, ui_handler, text="NEXT", widgetRow=-1, widgetCol=-1):
        # Call the ConnectedWidget constructor for shared initialization
        super().__init__(ui_handler, widgetRow, widgetCol)
        # Initialize the QPushButton part with the text
        QPushButton.__init__(self, text)

        # Connect the button's click event to the handler
        self.clicked.connect(lambda: ui_handler.ClickedNextTrack())


class PrevousTrackButtn(QPushButton, ConnectedWidget):
    def __init__(self, ui_handler, text="PREV", widgetRow=-1, widgetCol=-1):
        # Call the ConnectedWidget constructor for shared initialization
        super().__init__(ui_handler, widgetRow, widgetCol)
        # Initialize the QPushButton part with the text
        QPushButton.__init__(self, text)

        # Connect the button's click event to the handler
        self.clicked.connect(lambda: ui_handler.ClickedPrevTrack())







        
class SearchBarWidget(QLineEdit, ConnectedWidget):
    def __init__(self, ui_handler, text="Search...", widgetRow=-1, widgetCol=-1):
        # Initialize the ConnectedWidget to handle common properties
        super().__init__(ui_handler, widgetRow, widgetCol)
        # Initialize the QLineEdit with the given text
        QLineEdit.__init__(self, text)
        self.returnPressed.connect(lambda: self.find_update_objects_and_search())

     
    def find_update_objects_and_search(self):
        # objList = [SearchTextWidget, TrackTabel, AlbumsTabel, ArtistsTabel, PlaylistsTabel]
        # found_window_objs = find_Objects(self.window, objList)
        self.ui_handler.RunSearch(self.text())


class SearchTextWidget(QLabel, IsolatedWidget):
    def __init__(self, text="Result will appear here", widgetRow=-1, widgetCol=-1):
        # Initialize IsolatedWidget for handling row and column
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        
        # Initialize QLabel with the text
        QLabel.__init__(self, text)

        

        
        
        
        


from applicationTypes import TrackItem
# class SuperItems():
class TrackTableLabel(QLabel, IsolatedWidget):
    def __init__(self, text="track_label", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        QLabel.__init__(self, text)
        
class TrackTabel(QListWidget, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1):
        super().__init__(ui_handler, widgetRow, widgetCol)
        QListWidget.__init__(self)

        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item: TrackItem):
        print(f"TrackObject: {item}")
        self.ui_handler.ClickedTrack(item)
        
        # found_objs = find_Objects(self.window, [TrackArtworkWidget, TrackTitle, PlayButtn])
        # found_objs[0].setImage(item.cover_url)
        # found_objs[1].setText(item.name)
        # found_objs[2].set_as_playing()


class AlbumsTableLabel(QLabel, IsolatedWidget):
    def __init__(self, text="album_label", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        QLabel.__init__(self, text)
        
class AlbumsTabel(QListWidget, ConnectedWidget):
    def __init__(self,  ui_handler, widgetRow=-1, widgetCol=-1):
        super().__init__(ui_handler, widgetRow, widgetCol)
        QListWidget.__init__(self)

        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        print(f"AlbumObject: {item}")
        self.ui_handler.ClickedAlbum(item)


class ArtistsTableLabel(QLabel, IsolatedWidget):
    def __init__(self, text="artists_label", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        QLabel.__init__(self, text)

class ArtistsTabel(QListWidget, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1):
        super().__init__(ui_handler, widgetRow, widgetCol)
        QListWidget.__init__(self)

        
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        print(f"ArtistObject: {item}")
        self.ui_handler.ClickedArtist(item)




class PlaylistsTableLabel(QLabel, IsolatedWidget):
    def __init__(self, text="playlist_label", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        QLabel.__init__(self, text)
        
class PlaylistsTabel(QListWidget, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1):
        # Initialize the ConnectedWidget to handle common properties
        super().__init__(ui_handler, widgetRow, widgetCol)
        
        # Initialize the QListWidget part
        QListWidget.__init__(self)
        self.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, playlist_item):
        print(f"PlaylistObject: {playlist_item}")
        # found_objs = find_Objects(self.window, [PlaylistQueueLabel, PlaylistQueueTabel])
        # found_objs[0].setImage(item.cover_url)
        # found_objs[1].setText(item.name)
        self.ui_handler.ClickedPlaylist(playlist_item)



class PlaylistQueueLabel(QLabel, IsolatedWidget):
    def __init__(self, text="current_playlist_title", widgetRow=-1, widgetCol=-1):
        # Initialize DisconnectedWidget to handle widgetRow and widgetCol
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        
        # Initialize the QLabel with the provided text
        QLabel.__init__(self, text)
        
class PlaylistQueueTabel(QListWidget, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1):
        # Initialize the ConnectedWidget to handle common properties
        super().__init__(ui_handler, widgetRow, widgetCol)
        # Initialize the QListWidget part (no need for super call as we're using QListWidget directly)
        QListWidget.__init__(self)
        
        # self.setStyleSheet("""
        # QListWidget::item:selected {
        #     background-color: lightblue;
        #     color: black;
        # }
        # QListWidget::item {
        #     background-color: white;
        # }
        # """)
        
        self.index = -1
        self.itemClicked.connect(self.on_item_clicked)
        
        
    def on_item_clicked(self, item: QListWidgetItem):
        print(f"TrackObject From Queue Table: {item}")
        
        if item is not None:
            item.setSelected(True)
            self.index = self.get_index_from_item(item)
            self.ui_handler.ClickedTrack(item)
            print(f"itemINDEX: {self.index}")
        
        # found_objs = find_Objects(self.window, [TrackArtworkWidget, TrackTitle, PlayButtn])
        # found_objs[0].setImage(item.cover_url)
        # found_objs[1].setText(item.name)
        # found_objs[2].set_as_playing()

    def get_queue_size(self):
        return self.count()
    
    def get_index_from_item(self, item: QListWidgetItem):
        return self.indexFromItem(item).row()
    
    def get_item_from_index(self, index: int):
        return self.itemFromIndex(index)
    
    def get_next_item(self):
        """
        Add error handling for if next item is None
        - Alert UI of some how
        """
        print(f"+Changing Index to  {self.index+1}")
        next_item = self.item(self.index+1)
        self.itemClicked.emit(next_item)


            
    def get_prev_item(self):
        """
        Add error handling for if prev item is None
        - Alert UI of some How
        """
        self.prev_clicked = True
        print(f"-Changing Index to {self.index-1}")
        self.itemClicked.emit(self.item(self.index-1))
        
    
    
    

