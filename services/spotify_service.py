import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

class SpotifyService:
    def _authentification_spotify(self):
        load_dotenv()

        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')

        return SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    def get_spotify(self):
        authentification = self._authentification_spotify()

        return spotipy.Spotify(auth_manager=authentification)
