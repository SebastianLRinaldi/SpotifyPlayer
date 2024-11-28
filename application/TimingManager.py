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


import threading

# def setup_timer(self):
#     # make QTimer
#     self.qTimer = QTimer()
#     # set interval to 1 s
#     self.qTimer.setInterval(1000) # 1000 ms = 1 s

# class TimerManager:
#     def __init__(self):
#         self.is_running = False

#     def start(self):
#         self.is_running = True
#         self.thread = threading.Thread(target=self.run)
#         self.thread.start()

#     def stop(self):
#         self.is_running = False

#     def run(self):
#         while self.is_running:
#             # Implement timer logic here
#             pass

"""
Working but not what we need
"""
# class TimerManager(QObject):
#     # Signal to send progress updates to the widget
#     progress_signal = pyqtSignal(int)

#     def __init__(self):
#         super().__init__()
#         self.is_running = False
#         self.progress = 0  # Simulated progress value
    
#     def start(self):
#         self.is_running = True
#         self.thread = threading.Thread(target=self.run)
#         self.thread.start()

#     def stop(self):
#         self.is_running = False

#     def run(self):
#         while self.is_running and self.progress < 100:
#             # Simulate progress update
#             self.progress += 1
#             # Emit the signal to update the progress bar
#             self.progress_signal.emit(self.progress)
#             # Sleep for 1 second to simulate the passage of time
#             time.sleep(1)

"""
This was inside our Progressbar Widget
"""
        # # Create a TimerManager instance
        # self.timer_manager = TimerManager()
        
        # # Connect the progress_signal from TimerManager to update the progress bar
        # self.timer_manager.progress_signal.connect(self.update_progress)
        
        # # Start the timer manager to simulate progress
        # self.timer_manager.start()
        
    #     def update_progress(self, value):
        # """Update the progress bar's value"""
        
        # self.setValue(self.mwc.get_song_progress())
        # print(f"Progress: {value}%")


class TimerManager(QObject):
    # Signal to send progress updates to the widget
    progress_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.is_running = False
        self.progress = 0  # Simulated progress value
    
    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.is_running = False

    def run(self):
        while self.is_running and self.progress < 100:
            # Simulate progress update
            self.progress += 1
            # Emit the signal to update the progress bar
            self.progress_signal.emit(self.progress)
            # Sleep for 1 second to simulate the passage of time
            time.sleep(1)