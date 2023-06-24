import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication with the Spotify API
client_id = 'c4472c8627b94f65b798020c0e02a002'
client_secret = 'e0f06f05b9d34dd9834e32c1ffd4f343'
redirect_uri = 'http://localhost:8888/callback'
scope = 'playlist-modify-public'
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

# Get the URL to redirect the user to for authorization
auth_url = sp_oauth.get_authorize_url()

# Print out the URL to the console so you can see the authorization code
print(f"Please go to this URL to authorize the app: {auth_url}")

# Open the URL in a web browser and have the user authorize your app

# After the user authorizes your app, the Spotify API will redirect them to the redirect URI
# Your code should listen for the redirect and handle it by calling the get_access_token method on the SpotifyOAuth instance
code = input("Enter the authorization code: ")
token_info = sp_oauth.get_access_token(code)
access_token = token_info['access_token']