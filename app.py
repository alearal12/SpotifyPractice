from flask import Flask, jsonify
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_top_tracks():
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_top_tracks(lz_uri)
    
    tracks = []
    for track in results['tracks'][:10]:
        track_info = {
            'name': track['name'],
            'preview_url': track['preview_url'],
            'cover_art': track['album']['images'][0]['url']
        }
        tracks.append(track_info)

    return jsonify(tracks)

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()