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

from threading import Thread
import threading


"""
This needs to be in the app_strucuter file instead of the layouts file
"""
from MainWindowWidgetLayout import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(400, 300)
        self.setup_central_widget()

    def setup_central_widget(self, *widgets):
        grid_layout = GridLayout(*widgets)
        central_widget = Widget(grid_layout)
        self.setCentralWidget(central_widget)

    def show_window(self):
        self.show()
        

def run():
    app = QApplication(sys.argv)
    window = Window()
    
    window.setup_central_widget(
        SearchBar(window),
        SearchResultsTables(window),
        TrackInfoPanel(),
        PlayerControls(window),
        
    )
    
    window.show_window()
    app.exec_()       
    
def main():
    qt_thread = threading.Thread(target=run)
    qt_thread.start()
    
    sw = SpotifyWebViewController()
    sw.run()
if __name__ == "__main__":
    main()