import spotipy
import os
from dotenv import load_dotenv 
import spotipy.oauth2 as spotOauth
import sys

load_dotenv()

sp = spotipy.Spotify(auth_manager=spotOauth.SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"), 
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"), 
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URL"), 
    scope="user-read-playback-state user-modify-playback-state"
))

