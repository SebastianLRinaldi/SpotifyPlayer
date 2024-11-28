import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PyQt5.QtWidgets import QListView, QListWidgetItem, QMessageBox, QMainWindow

class Constants:
    SCOPE = 'user-library-read' #["user-read-playback-state", "user-modify-playback-state"] 'user-library-read' # 'streaming' # 'playlist-read-private' or 'user-library-read'
    TIMEOUT = 60  # seconds

    

class TrackItem(QListWidgetItem):
    def __init__(self, name, artist, cover_url, id):
        super().__init__("")
        self.name = name
        self.artist = artist
        self.cover_url = cover_url
        self.id = id
        self.setText(f"{name} - {artist} ({id})")
        
    def __str__(self):
        return f"<TrackItem '{self.name}' by {self.artist}, ID: {self.id} | IMG:{self.cover_url} >"
    

class AlbumItem(QListWidgetItem):
    def __init__(self, name, artist, id):
        super().__init__("")
        self.name = name
        self.artist = artist
        self.id = id
        self.setText(f"Album: {name} by {artist} ({id})")

    def __str__(self):
        return f"<AlbumItem '{self.name}' by {self.artist}, ID: {self.id}>"


class ArtistItem(QListWidgetItem):
    def __init__(self, name, popularity, genres):
        super().__init__("")
        self.name = name
        self.popularity = popularity
        self.genres = genres
        self.setText(f"Artist: {name} (Pop: {popularity}, Genres: {', '.join(genres)})")

    def __str__(self):
        return f"<ArtistItem '{self.name}', Pop: {self.popularity}, Genres: {self.genres}>"

class PlaylistItem(QListWidgetItem):
    def __init__(self, name, owner, total_tracks, id):
        super().__init__("")
        self.name = name
        self.owner = owner
        self.total_tracks = total_tracks
        self.id = id
        self.setText(f"Playlist: {name} by {owner}, Total tracks: {total_tracks}, ID: {id}")

    def __str__(self):
        return f"<PlaylistItem '{self.name}', Owner: {self.owner}, Total tracks: {self.total_tracks}, ID: {self.id}>"
