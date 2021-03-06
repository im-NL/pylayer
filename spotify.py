import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# ---------------------TO DO ---------------------------- 
#   make a get_name command to get name from spotify link for a single song
#   and make it program faster
# --------------------------------------------------------


client = 'client key' 
secret = 'secret key'

client_credentials_manager = SpotifyClientCredentials(client_id=client, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_tracks(url):
    results = spotify.playlist_tracks(url)
    result = []
    for i in range(len(results['items'])):
        result.append(results['items'][i]['track']['name'] + ' ' + results['items'][i]['track']['artists'][0]['name'])

    return result
