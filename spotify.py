import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# ---------------------TO DO ---------------------------- 
#   make a get_name command to get name from spotify link
# --------------------------------------------------------


client = '3298160dcfbd4f98bab39a3361036577' 
secret = '38b00c4aeb664bb3af894c7b1dd270bf'

client_credentials_manager = SpotifyClientCredentials(client_id=client, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_tracks(url):
    results = spotify.playlist_tracks(url)
    result = []
    for i in range(len(results['items'])):
        result.append(results['items'][i]['track']['name'] + ' ' + results['items'][i]['track']['artists'][0]['name'])

    return result
