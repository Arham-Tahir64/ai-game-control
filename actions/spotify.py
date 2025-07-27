import spotipy
import os
from dotenv import load_dotenv 
import spotipy.oauth2 as spotOauth
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from llm.reqests import combat_status, classification

load_dotenv()

sp = spotipy.Spotify(auth_manager=spotOauth.SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"), 
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"), 
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URL"), 
    scope="user-read-playback-state user-modify-playback-state"
))

# Current playing track
current = sp.current_playback()
if current and current['is_playing']:
    print("Now Playing:", current['item']['name'], "by", current['item']['artists'][0]['name'])
else:
    print("Nothing is currently playing.")

    
# Volume logic
status = combat_status(classification)

if status is True:
    print("Turn volume down")
    sp.volume(0)
elif status is False:
    print("Turn volume up")
    sp.volume(100)
else:
    print("Unrecognized classification, no volume change.")
