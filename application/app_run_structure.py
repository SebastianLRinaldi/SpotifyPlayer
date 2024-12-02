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
Should add a current duration timmer on player panel 
Should show album/playlist title on player alumb or show that its a playlist?
or at least its loaded and playing from the queue
"""
from MainWindowWidgetLayout import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(1000, 600)
        self.setup_stylesheets()


    def setup_central_widget(self, *widgets):
        grid_layout = GridLayout(*widgets)
        central_widget = Widget(grid_layout)
        self.setCentralWidget(central_widget)

    def show_window(self):
        self.show()
        
    def setup_stylesheets(self):
        """
        Apply styles directly to the QMainWindow and its children.
        """
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2f; /* Dark background */
            }
            QLabel {
                color: #E6E6FA; /* Light Purple */
                font-weight: bold;
            }
            QLineEdit {
                background-color: #2c2c3b;
                color: #D8BFD8; /* Light Purple */
                border: 1px solid #D8BFD8;
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
            }

            QListWidget {
                background-color: #2c2c3b; /* Darker background for list */
                color: #E6E6FA; /* Light Purple text */
                border: 1px solid #D8BFD8; /* Light Purple Border */
                border-radius: 10px;
                padding: 5px;
            }

            QListWidget::item {
                background-color: #2c2c3b; /* Match background */
                color: #D8BFD8; /* Light Purple for list items */
                border: none;
                padding: 5px;
            }

            QListWidget::item:selected {
                background-color: #D8BFD8; /* Light Purple for selected item */
                color: #1e1e2f; /* Dark text for contrast */
                border-radius: 5px;
            }

            QTabWidget::pane {
                background-color: #1e1e2f; /* Match background with main window */
                border: 1px solid #D8BFD8; /* Light Purple Border */
                border-radius: 10px;
            }

            QTabWidget::tab-bar {
                alignment: center;
            }

            QTabBar::tab {
                background: #2c2c3b; /* Darker background for tabs */
                color: #D8BFD8; /* Light Purple text */
                border: 1px solid #D8BFD8;
                border-radius: 10px;
                padding: 5px;
                margin: 2px;
            }

            QTabBar::tab:selected {
                background: #D8BFD8; /* Highlight active tab */
                color: #1e1e2f; /* Dark text on active tab */
            }

            QTabBar::tab:hover {
                background: #E6E6FA; /* Lighter Purple on hover */
            }
            
            QPushButton {
                background-color: #D8BFD8; /* Light Purple */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #E6E6FA; /* Lighter Purple on Hover */
            }
            QProgressBar {
                text-align: center;
                background-color: #2c2c3b;
                border: 1px solid #D8BFD8;
                border-radius: 10px;
                height: 8px;
                font-size: 12px;
            }
            QProgressBar::chunk {
                background-color: #E6E6FA; /* Light Purple Chunk */
                border-radius: 5px;
            }
        """)
        



def run_pyqt(win):
    app = QApplication(sys.argv)
    window = Window()
    
    exploreTab = Tab(window, widgetRow=0, widgetCol=0)
    playTab = Tab(window, widgetRow=0, widgetCol=1)
    
    """
    Gotta add some way to save good tracks that I find 
    Make and play playlist from my spotify account
    """
    
    
    exploreTab.add_widges_to_tab(
                SearchBar(window), 
                SearchResultsTables(window),
                title="Search")
    
    exploreTab.add_widges_to_tab(
                PlayerQueue(window),
                title="Queue")
    
    exploreTab.add_widges_to_tab(
            DebugPanel(window),
            title="Debug"
            )
    
    playTab.add_widges_to_tab(
                TrackInfoPanel(window),
                PlayerControls(window),
                title="Player Panel")
    
    playTab.add_widges_to_tab(
                TrackDetailsPanel(window),
                title="Track Details"
                )
    
    
    window.setup_central_widget(
        exploreTab,
        playTab,
    )
    
    window.show_window()
    app.exec_()     


    
def main():
    SpotifyWebViewMaker().run_win(run_pyqt)
if __name__ == "__main__":
    main()