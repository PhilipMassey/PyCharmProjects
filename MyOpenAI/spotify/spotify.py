import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

csv_file = '/Users/philipmassey/Downloads/spotify.csv'
songs = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        songs.append(row)


# Set up authentication with the Spotify API
client_id = 'c4472c8627b94f65b798020c0e02a002'
client_secret = 'e0f06f05b9d34dd9834e32c1ffd4f343'
redirect_uri = 'http://localhost:8888/callback'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for each song on Spotify and get its URI
for song in songs:
    query = f"track:{song['song']} artist:{song['artist']}"
    results = sp.search(query, type='track')
    if results['tracks']['items']:
        uri = results['tracks']['items'][0]['uri']
        song['uri'] = uri

# Create a new playlist on Spotify
playlist_name = 'Can you hear me knocking'
username = sp.current_user()['id']
playlist = sp.user_playlist_create(username, playlist_name)

# Get the URI of the new playlist
playlist_uri = playlist['uri']        

# Add the songs to the new playlist
sp.user_playlist_add_tracks(username, playlist_uri, [song['uri'] for song in songs])
    