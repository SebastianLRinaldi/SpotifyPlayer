import PyQt5 
from PyQt5.QtWidgets import QListView, QListWidgetItem, QMessageBox, QMainWindow
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
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
from PyQt5.QtWidgets import QApplication
import threading
from queue import Queue
import spotipy
from spotipy.oauth2 import SpotifyOAuth


"""
Will need to use something called pub/sub method for getting ui elements to talk together
"""
'''
UI Compenets made with widgets this needs to be here in this file
'''

from WidgetDefinitions import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit, QGridLayout



"""
Gets Updated by other elements and needs to access other UI elements
"""
class PlayerControls(QWidget):
    def __init__(self, window: QMainWindow,):
        super().__init__()
        
        grid_layout = GridLayout(
            PlayButtn(window),
            PrevousTrackButtn(),
            NextTrackButtn()
            )
        
        self.setLayout(grid_layout)

"""
Gets Updated by other elements but don't need to access other UI elements
"""      
class TrackInfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        
        grid_layout = GridLayout(
            TrackArtworkWidget(),
            TrackProgressWidget(),
            TrackTitle()
            )
        
        self.setLayout(grid_layout)
        
"""
Gets Updated by other elements and needs to access other UI elements
"""       
class SearchBar(QWidget):
    def __init__(self, window: QMainWindow):
        super().__init__()
        
        grid_layout = GridLayout(
            SearchBarWidget(window),
            SearchTextWidget()
            )
        
        self.setLayout(grid_layout)

"""
Gets Updated by other elements and needs to access other UI elements
"""
class SearchResultsTables(QWidget):
    def __init__(self, window: QMainWindow):
        super().__init__()
        
        grid_layout = GridLayout(
            TrackTableLabel(),
            TrackTabel(window),
            AlbumsTableLabel(),
            AlbumsTabel(window),
            ArtistsTableLabel(),
            ArtistsTabel(window),
            PlaylistsTableLabel(),
            PlaylistsTabel(window),
            )
        
        self.setLayout(grid_layout)       
        
        
'''
Layout controlers
'''      
class GridLayout(QGridLayout):
    def __init__(self, *widgets):
        super().__init__()  # No arguments here
        for i, widget in enumerate(widgets):
            row = i // 1
            col = i % 1
            self.addWidget(widget, row, col)

class Widget(QWidget):
    def __init__(self, layout=None):
        super().__init__()
        if layout:
            self.setLayout(layout)


