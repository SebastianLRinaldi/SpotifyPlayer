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


from TimingManager import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from WidgetDefinitions import ConnectedWidget, IsolatedWidget
from WebviewManager import WebviewDOM



class DebugElementWidget(QLineEdit, ConnectedWidget):
    def __init__(self, ui_handler, text="Search...", widgetRow=-1, widgetCol=-1):
        # Initialize the ConnectedWidget to handle common properties
        super().__init__(ui_handler, widgetRow, widgetCol)
        # Initialize the QLineEdit with the given text
        QLineEdit.__init__(self, text)
        self.returnPressed.connect(lambda: self.find_update_objects_and_search())

    def find_update_objects_and_search(self):
        # objList = [SearchTextWidget, TrackTabel, AlbumsTabel, ArtistsTabel, PlaylistsTabel]
        # found_window_objs = find_Objects(self.window, objList)
        # self.ui_handler.RunSearch(self.text())
        try:
            WebviewDOM().mark_element(self.text())
        except Exception as e:
            print(f"ERROR Marking Element!: \n\t{e}")
            


class DebugElementResultWidget(QLabel, IsolatedWidget):
    def __init__(self, text="Result will appear here", widgetRow=-1, widgetCol=-1):
        # Initialize IsolatedWidget for handling row and column
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        
        # Initialize QLabel with the text
        QLabel.__init__(self, text)

    def somethingfunny(self):
        """ A custom method for something funny. """
        print("SOMETHING FUNNY")