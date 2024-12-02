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

import WebviewManager
from TimingManager import TimerManager
from WebviewManager import WebviewWindow, WebviewDOM




'''
Need to split the window creation and the spotify webapge manipuluation into two classes
'''
class SpotifyWebViewMaker:
    def __init__(self):
        pass
    
    def run_win(self, backend_logic):
        self.create_window(backend_logic)
        

    def create_window(self, backend_logic):
        default_url = "https://open.spotify.com/embed/track/0B7zVYoRimfnl1RqmFNksV"
        WebviewWindow().set_and_start_window(backend_logic, default_url)

        
class SpotifyWebViewController:
    def __init__(self):
        pass

    def load_song(self, song_type: str, song_id: str):
        song_url = self.get_song_url(song_type, song_id)
        # print(f"MADE URL: {song_url} | len{len(song_url)} | type:{type(song_url)} ")
        WebviewWindow().change_url(song_url)

    def get_song_url(self, song_type, song_id):
        # print(f"type {song_type} | id {song_id}")
        if song_type == 'track':
            return f"https://open.spotify.com/embed/track/{song_id}"
        elif song_type == 'playlist':
            print(f"https://open.spotify.com/embed/playlist/{song_id}?utm_source=generator&theme=0")
            return f"https://open.spotify.com/embed/playlist/{song_id}?utm_source=generator&theme=0"
        elif song_type == 'album':
            return f"https://open.spotify.com/embed/album/{song_id}?utm_source=generator&theme=0"

    def mark_important_elements(self):
        WebviewDOM().mark_element('data-testid="play-pause-button"', color='green')
        WebviewDOM().mark_element('data-testid="control-button-skip-back"')
        WebviewDOM().mark_element('data-testid="control-button-skip-forward"')
        WebviewDOM().mark_element('class="playback-bar"', color='purple')
        WebviewDOM().mark_element('data-testid="playback-position"', color='blue')
        WebviewDOM().mark_element('data-testid="playback-duration"', color='blue')
        WebviewDOM().mark_element('data-testid="playback-progressbar"', color='orange')
        WebviewDOM().mark_element('data-testid="progress-bar-slider"', color='cyan')

    def track_progress(self):
        progress_number_result = 0
        progress_element, selector = WebviewDOM().find_element('[data-testid="progress-bar-slider"]')
        if progress_element:
            progress_value = progress_element.attributes["style"]
            value_stripped = progress_value.split()[1].strip('%;')
            progress_as_float = float(value_stripped)
            progress_as_int = int(progress_as_float)
            # print(progress_as_int)
            # print(progress_as_float)
            progress_number_result = progress_as_int
        return (progress_number_result)
    
    def track_time_progress(self):
        stripped_time_element = "00:00"
        time_element, selector = WebviewDOM().find_element('[data-testid="progress-timestamp"]')
        if time_element:
            # print(f"Stripped: {time_element.text.strip()[1:]}")
            stripped_time_element  = time_element.text.strip()[1:]
        return stripped_time_element #(progress_number_result)

    def click_play_btn(self):

        iteration_count = 0
        max_iterations = 20  # Maximum number of attempts
        element = None
        playbtnresult = "Not Found"
        while iteration_count < max_iterations and element is None:
            iteration_count += 1
            
            # Your action here
            print(f"Checking iteration {iteration_count}")
            
            element, selector = WebviewDOM().find_element('[data-testid="play-pause-button"]')
            

            if element is not None:
                print(element.attributes['aria-label'])
                # print("Found element:", element.tag)
                # Should return 'play', 'pause', or 'Something went wrong'
                playbtnresult = element.attributes['aria-label']
                
                # Add button click functionality
                js_code = f'''
                var element = document.querySelector('{selector}');

                element.click();
                '''
                # Execute the JavaScript code
                result = webview.windows[0].evaluate_js(js_code)
            else:
                print(f"Contining to Find Play Button | {iteration_count} out of {max_iterations}")
                time.sleep(0.25)
            # If not found, continue with next iteration

        if iteration_count == max_iterations:
            print("Element not found after maximum attempts")
            
        return playbtnresult




