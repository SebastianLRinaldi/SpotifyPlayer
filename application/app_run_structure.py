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






from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QLinearGradient, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QVariantAnimation, QPropertyAnimation, pyqtProperty, QPoint
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient
import random

class CRTOverlayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Make the widget transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setGeometry(0, 0, parent.width(), parent.height())  # Full size overlay

        self.red_offset = 0
        self.blue_offset = 0
        self.yellow_offset = 0
        
        # Initialize flicker opacity
        self._opacity = 255  # Set initial opacity to 1 (fully visible)

        # Set up flicker animation with keyframes
        self.flicker_animation = QVariantAnimation(self)
        self.flicker_animation.setStartValue(self._opacity)
        self.flicker_animation.setEndValue(self._opacity)  # Start and end with initial value, we'll update manually
        self.flicker_animation.setDuration(150)  # Duration for the whole cycle (in milliseconds)
        self.flicker_animation.setLoopCount(-1)  # Loop indefinitely
        
        # Define keyframe-like opacity values (from your CSS flicker)
        self.flicker_animation.setKeyValueAt(0.0, 0.95)  # Start at the highest opacity
        self.flicker_animation.setKeyValueAt(0.1, 0.91)  # Slight drop
        self.flicker_animation.setKeyValueAt(0.2, 0.93)  # Bounce back up
        self.flicker_animation.setKeyValueAt(0.3, 0.87)  # Subtle drop
        self.flicker_animation.setKeyValueAt(0.4, 0.91)  # Slight rise
        self.flicker_animation.setKeyValueAt(0.5, 0.93)  # Bounce back up
        self.flicker_animation.setKeyValueAt(0.6, 0.87)  # Slight drop
        self.flicker_animation.setKeyValueAt(0.7, 0.89)  # Subtle rise
        self.flicker_animation.setKeyValueAt(0.8, 0.87)  # Gentle drop
        self.flicker_animation.setKeyValueAt(0.9, 0.92)  # Slight rise
        self.flicker_animation.setKeyValueAt(1.0, 0.95)  # End at the highest opacity

        # Connect the animation's value change signal to a function that updates the opacity
        self.flicker_animation.valueChanged.connect(self.update_opacity)
        
        # Start the animation
        self.flicker_animation.start()
        


        # Set up color separation animation with start and end values
        self.color_animation = QPropertyAnimation(self, b"colorOffsets")
        self.color_animation.setDuration(1600)  # Animation duration for color offset
        self.color_animation.setStartValue(QPoint(int(self.red_offset), int(self.blue_offset)))
        self.color_animation.setEndValue(QPoint(int(random.uniform(-3, 3)), int(random.uniform(-3, 3))))  # Randomize end values for offsets
        self.color_animation.setLoopCount(-1)  # Loop indefinitely
        self.color_animation.start()

    @pyqtProperty(int)
    def opacity(self):
        return self._opacity
    
    @opacity.setter
    def opacity(self, value):
        self._opacity = value
        self.update()  # Trigger a repaint

    @pyqtProperty(QPoint)
    def colorOffsets(self):
        return QPoint(int(self.red_offset), int(self.blue_offset))

    @colorOffsets.setter
    def colorOffsets(self, value):
        self.red_offset = value.x()  # Use x() for red offset
        self.blue_offset = value.y()  # Use y() for blue offset
        self.yellow_offset = random.uniform(-3, 3)  # Randomize yellow offset
        self.update()  # Trigger repaint

    def update_opacity(self, value):
        # Update the opacity value with the one from the animation
        self._opacity = value
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        super().paintEvent(event)

        # Get text details
        text = "Text"
        rect = self.rect()

        # Set font for custom drawing
        font = QFont("Arial", 36)
        painter.setFont(font)


        painter.setOpacity(1)
        # First, draw the text with shadows (color separation)
        # Draw blue shadow
        blue_offset_int = int(self.blue_offset)  # Cast to int
        painter.setPen(QColor(0, 30, 255, 128))  # Blue with transparency
        painter.drawText(rect.adjusted(blue_offset_int, 0, blue_offset_int, 0), Qt.AlignCenter, text)

        # Draw red shadow
        red_offset_int = int(self.red_offset)  # Cast to int
        painter.setPen(QColor(255, 0, 80, 128))  # Red with transparency
        painter.drawText(rect.adjusted(-red_offset_int, 0, -red_offset_int, 0), Qt.AlignCenter, text)

        # Draw yellow shadow
        yellow_offset_int = int(self.yellow_offset)  # Cast to int
        painter.setPen(QColor(255, 255, 0, 128))  # Yellow with transparency
        painter.drawText(rect.adjusted(0, yellow_offset_int, 0, yellow_offset_int), Qt.AlignCenter, text)

        # Draw the main white text
        painter.setPen(Qt.white)
        painter.drawText(rect, Qt.AlignCenter, text)

        # Control opacity using QPainter
        painter.setOpacity(self._opacity)  # Use the set opacity
        # Apply a CRT-like gradient overlay
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(1, QColor(0, 120, 90, 80))  # Soft blue color
        gradient.setColorAt(0.3, QColor(150, 50, 200, 80))  # Soft purple color
        painter.fillRect(self.rect(), gradient)

        # Add scanline effect
        for y in range(0, self.height(), 2):
            painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 100))  # Less intense scanlines

        painter.end()

"""
Should add a current duration timmer on player panel 
Should show album/playlist title on player alumb or show that its a playlist?
or at least its loaded and playing from the queue
"""
from MainWindowWidgetLayout import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QLinearGradient, QColor
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(1000, 600)
        self.setup_stylesheets()
        
    def add_overlay(self):
        pass
        # Add the CRT overlay widget
        # self.overlay = CRTOverlayWidget(self)
        # self.overlay.raise_()  # Ensure overlay is on top
        # self.overlay.show()


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
        background-color: #1a0d1c;
        
    }
    QLabel {
        color: #f6e2f8;
        font-weight: bold;
        font-size: 18px;
    }
    QLineEdit {
        background-color: #1a0d1c;
        color: #f6e2f8;
        border: 1px solid #79253e;
        border-radius: 10px;
        padding: 5px;
        font-size: 18px;
    }
    QListWidget {
        background-color: #1a0d1c;
        color: #f6e2f8;
        border: 1px solid #79253e;
        border-radius: 10px;
        padding: 5px;
        font-size: 16px;
    }
    QListWidget::item {
        background-color: #1a0d1c;
        color: #f6e2f8;
        border: none;
        padding: 5px;
    }
    QListWidget::item:selected {
        background-color: #79253e;
        color: #1a0d1c;
        border-radius: 5px;
    }
    QTabWidget::pane {
        background-color: #1a0d1c;
        border: 1px solid #79253e;
        border-radius: 10px;
    }
    QTabWidget::tab-bar {
        alignment: center;
    }
    QTabBar::tab {
        background: #79253e;
        color: #f6e2f8;
        border: 1px solid #79253e;
        border-radius: 10px;
        padding: 5px;
        margin: 2px;
        min-height: 30px; /* Adjust as needed */
        min-width: 100px; /* Adjust based on content length */
        font-size: 18px;
    }
    QTabBar::tab:selected {
        background: #79253e;
        color: #f6e2f8;
    }
    QTabBar::tab:hover {
        background: #d26076;
    }
    QPushButton {
        background-color: #79253e;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 16px;
        font-size: 24px;
    }
    QPushButton:hover {
        background-color: #d26076;
    }
    QProgressBar {
        text-align: center;
        background-color: #79253e;
        border: 1px solid #79253e;
        border-radius: 10px;
        height: 8px;
        font-size: 24px;
        padding: 12px;
    }
    QProgressBar::chunk {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                    stop:0.1 #290D12,
                                    stop:0.2 #341118,
                                    stop:0.3 #42161E,
                                    stop:0.4 #541C27,
                                    stop:0.5 #6B2533,
                                    stop:0.6 #893042,
                                    stop:0.7 #AE3F55,
                                    stop:0.8 #C55C71,
                                    stop:0.9 #D78A99,
                                    stop:1 #EBC3CB
                                    );
                        }
        border-radius: 5px;
        width: 20px;
        margin: 1px;
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
    window.add_overlay()
    window.show_window()
    app.exec_()     


    
def main():
    SpotifyWebViewMaker().run_win(run_pyqt)
if __name__ == "__main__":
    main()