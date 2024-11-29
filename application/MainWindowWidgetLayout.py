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
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            PlayButtn(window),
            PrevousTrackButtn(),
            NextTrackButtn()
            )
        
        self.setLayout(grid_layout)
        
        
        
class PlayerQueue(QWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            PlaylistQueueLabel(),
            PlaylistQueueTabel(window)
            )
        
        self.setLayout(grid_layout)

"""
Gets Updated by other elements but don't need to access other UI elements
"""      
class TrackInfoPanel(QWidget):
    def __init__(self,widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            TrackArtworkWidget(),
            TrackProgressWidget(),
            TrackTitle()
            )
        
        self.setLayout(grid_layout)
        
        
class TrackDetailsPanel(QWidget):
    def __init__(self,widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            TrackArtworkWidget(),
            TrackTitle(),
            TrackArtist(),
            TrackID(),
            TrackDuration(),
            TrackPopularity()
            )
        
        self.setLayout(grid_layout)
        
"""
Gets Updated by other elements and needs to access other UI elements
"""       
class SearchBar(QWidget):
    def __init__(self, window: QMainWindow, widgetRow = 0, widgetCol = 0):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            SearchBarWidget(window),
            SearchTextWidget()
            )
        
        self.setLayout(grid_layout)

"""
Gets Updated by other elements and needs to access other UI elements
"""
class SearchResultsTables(QWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
        grid_layout = GridLayout(
            TrackTableLabel(widgetRow = 0, widgetCol = 0),
            TrackTabel(window, widgetRow = 1, widgetCol = 0),
            
            AlbumsTableLabel(widgetRow = 0, widgetCol = 1),
            AlbumsTabel(window, widgetRow = 1, widgetCol = 1),
            
            ArtistsTableLabel(widgetRow = 2, widgetCol = 0),
            ArtistsTabel(window, widgetRow = 3, widgetCol = 0),
            
            PlaylistsTableLabel(widgetRow = 2, widgetCol = 1),
            PlaylistsTabel(window, widgetRow = 3, widgetCol = 1),
            )
        
        self.setLayout(grid_layout)       
        
        
'''
Layout controlers
'''
class Tab(QTabWidget):
    def __init__(self, window: QMainWindow, widgetRow = -1, widgetCol = -1):
        super().__init__()
        self.parent = window
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
    def add_widges_to_tab(self, *widgets, title="New Tab"):
        new_tab = QWidget()
        layout = QGridLayout(new_tab)
        
        for i, widget in enumerate(widgets):
            widgetRow = widget.widgetRow #i // 1
            widgetCol = widget.widgetCol#i % 1
            
            print(f'TAB: {type(widget)}')
            if widgetRow == -1 or widgetCol == -1:
                widgetRow = i // 1
                widgetCol = i % 1
                layout.addWidget(widget, widgetRow, widgetCol)
            else:
                layout.addWidget(widget, widgetRow, widgetCol)
            
        self.addTab(new_tab, title)

class GridLayout(QGridLayout):
    def __init__(self, *widgets):
        super().__init__()  # No arguments here
        for i, widget in enumerate(widgets):
            widgetRow = widget.widgetRow #i // 1
            widgetCol = widget.widgetCol#i % 1
            
            print(f'WIDGET: {type(widget)}')
            if widgetRow == -1 or widgetCol == -1:
                widgetRow = i // 1
                widgetCol = i % 1
                self.addWidget(widget, widgetRow, widgetCol)
            else:
                self.addWidget(widget, widgetRow, widgetCol)

class Widget(QWidget):
    def __init__(self, layout=None):
        super().__init__()
        if layout:
            self.setLayout(layout)


    

