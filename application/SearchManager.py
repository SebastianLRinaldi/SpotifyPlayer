from applicationTypes import *
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
from dotenv import load_dotenv



class SearchManager:
    def __init__(self):
        # Load the environment variables from the .env file
        load_dotenv()
        self.client_id =  os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.scope = Constants.SCOPE
        self.auth_manager = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope
        )
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        

    def search_and_process_using_spotify_api(self, query):
        # os.system('cls')
        results = self.sp.search(q=query, limit=10, type='track,album,artist,playlist')
        # print(results)
        self.process_results(results)

    def process_results(self, results):
        self.tracks = results['tracks']['items']
        self.albums = results['albums']['items']
        self.artists = results['artists']['items']
        self.playlists = results['playlists']['items']
    
        
    def clear_all_objs(self, objects_to_update: List[QObject]):
        for obj in objects_to_update:
            obj.clear()
        
    def add_track_items_to_table(self, tableToUpdate: QListWidget):
        try:
            # Tracks loop
            for i, track in enumerate(self.tracks):
                # print(f'\nTRACK: {track}\n')
                # print("\nREAL TRACK\n")
                # print(track.keys())
                """
                track.keys() --> ['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'is_playable', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri']
                track['album'].keys() --> ['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'is_playable', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri']
                track['album']['images'] --> just a list of {}, no keys
                track['album']['images'][0].keys() --> ['height', 'width', 'url'] 
                ([0] --> 640X640)
                ([1] --> 300X300)
                ([2] --> 64X64)
                track['album']['images'][0]['url'] --> image url
                """
                
                name = track['name']
                artist = track['artists'][0]['name']
                duration = track['duration_ms']
                popularity = track['popularity']
                cover_url = track['album']['images'][1]['url']
                track_id = track['id']
                found_item = TrackItem(name, artist, duration, popularity, cover_url, track_id)
                #object_to_update.setText("FOUND TRACK") 
                tableToUpdate.addItem(found_item)
                # print(found_item)
        except Exception as e:
            print(f"Error placing items in TRACK table: {e}")
            
            
    def add_album_items_to_table(self, tableToUpdate: QListWidget):
        try:
            # Albums loop  
            for album in self.albums:
                found_item = AlbumItem(album['name'], album['artists'][0]['name'], album['id'])
                tableToUpdate.addItem(found_item)
                # print(found_item)
                
        except Exception as e:
            print(f"Error placing items in ALBUM table: {e}")
            
            
    def add_artist_items_to_table(self, tableToUpdate: QListWidget):
        try:
            # Artists loop
            """
            ['external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity', 'type', 'uri']
            """
            for artist in self.artists:
                found_item = ArtistItem(artist['name'], artist['popularity'], artist['genres'])
                tableToUpdate.addItem(found_item)
                # print(found_item)
        except Exception as e:
            print(f"Error placing items in ARTIST table: {e}")
            
    def add_playlist_items_to_table(self, tableToUpdate: QListWidget):
        try:
            # Playlists loop

            for playlist in self.playlists:
                found_item = PlaylistItem(playlist['name'], playlist['owner']['display_name'], playlist['tracks']['total'], playlist['id'])
                tableToUpdate.addItem(found_item)
                print(found_item)
                # pl_results = self.sp.playlist_tracks(playlist['id'], limit=5)
                # print(pl_results['items'][0]['track']['id'])
        except Exception as e:
            print(f"Error placing items in PLAYLIST table: {e}")
        


    def perform_search(self, search_query, objects_to_update: List[QObject]):
            
            self.clear_all_objs(objects_to_update)
            
            # search_text = objects_to_update[0]
            tracks_table = objects_to_update[1]
            albums_table = objects_to_update[2]
            artists_table = objects_to_update[3]
            playlists_table = objects_to_update[4]

            if search_query:
                # Add your search logic here
                result = f"Searching for: {search_query}"
                # print(result)
                objects_to_update[0].setText(result)

                try:
                    self.search_and_process_using_spotify_api(search_query)
                except Exception as e:
                    print(f"Error fetching the songs during search: {e}")
                
                self.add_track_items_to_table(tracks_table)
                self.add_album_items_to_table(albums_table)
                self.add_artist_items_to_table(artists_table)
                self.add_playlist_items_to_table(playlists_table)
    
    
    def search_and_process_tracks_only_using_spotify_api(self, playlist_id):
        # os.system('cls')
        pl_results = self.sp.playlist_tracks(playlist_id, limit=10)
        self.process_only_track_results(pl_results)
    
    """
    Fix when 'NoneType' object is not subscriptable
    
    pl_results['items'][0].keys() --> ['added_at', 'added_by', 'is_local', 'primary_color', 'track', 'video_thumbnail']
    pl_results['items'][0]['track'].keys() --> ['preview_url', 'available_markets', 'explicit', 'type', 'episode', 'track', 'album', 'artists', 'disc_number', 'track_number', 'duration_ms', 'external_ids', 'external_urls', 'href', 'id', 'name', 'popularity', 'uri', 'is_local']
    """
    def process_only_track_results(self, playlist_tracks):
        print("\n-------ONLY TACK RESULTS--------\n")
        # print(playlist_tracks['items'])
        # print("\n-------")
        # print(playlist_tracks['items'][0])
        # print("\n-------")
        # print(playlist_tracks['items'][0]['track'])
        # print("\n-------")
        # print(playlist_tracks['items'][0]['track']['id'])
        # print("\n-------")
        self.tracks = playlist_tracks['items']
    
    
    def add_track_items_to_queue_table(self, tableToUpdate: QListWidget):
        try:
            # Tracks loop
            for i, track in enumerate(self.tracks):
                # print(f'\nTRACK: {track}\n')
                # print("___________")
                # print(track["track"].keys())
                """
                track.keys() --> ['added_at', 'added_by', 'is_local', 'primary_color', 'track', 'video_thumbnail']
                track["Track"].keys() --> ['preview_url', 'available_markets', 'explicit', 'type', 'episode', 'track', 'album', 'artists', 'disc_number', 'track_number', 'duration_ms', 'external_ids', 'external_urls', 'href', 'id', 'name', 'popularity', 'uri', 'is_local']

                """
                track_root = track["track"]
                name = track_root['name'] 
                artist = track_root['artists'][0]['name']
                duration = track_root['duration_ms']
                popularity = track_root['popularity']
                cover_url = track_root['album']['images'][1]['url']
                track_id = track_root['id']
                found_item = TrackItem(name, artist, duration, popularity, cover_url, track_id)
                #object_to_update.setText("FOUND TRACK") 
                tableToUpdate.addItem(found_item)
                # print(found_item)
        except Exception as e:
            print(f"Error placing items in TRACK table: {e}")
    
    def perform_queue_loading(self, playlist_item, objects_to_update: List[QObject]):
            """
            Seperat Button on queue tab that will have this function to clear the queue
            """
            self.clear_all_objs(objects_to_update)
            
            playlist_title = objects_to_update[0]
            playlist_title.setText(playlist_item.name)
            queue_table = objects_to_update[1]


            try:
                self.search_and_process_tracks_only_using_spotify_api(playlist_item.id)
            except Exception as e:
                print(f"Error fetching the songs during search: {e}")
            
            self.add_track_items_to_queue_table(queue_table)
    
    