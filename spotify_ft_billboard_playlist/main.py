import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date_input = input("Which date do you want to travel back to? Type in the following format YYYY-MM-DD: ")
# date_input = '2000-08-12'
billboard_100 = 'https://www.billboard.com/charts/hot-100/'

response = requests.get(billboard_100+date_input)

soup = BeautifulSoup(response.text, 'html.parser')

#VERSION find_all
chart_items = soup.find_all(name='li', class_='o-chart-results-list__item')

titles = []
artists = []

for item in chart_items:
    title_element = item.find(name='h3', class_='c-title')
    artist_element = item.find(name='span', class_='c-label')
    
    if title_element and artist_element:
        title = title_element.text.strip()
        artist = artist_element.text.strip()
        titles.append(title)
        artists.append(artist)

# #VERSION select BUT it doesnt work for artist name because there are other elements following the same selectors
# title_names = soup.select("li ul li h3")
# titles = [song.getText().strip() for song in title_names]

# # artist_names = soup.select("li ul li span")
# # artists = [artist.getText().strip() for artist in artist_names]

song_list = [f"{song_title} - {artist}" for song_title, artist in zip(titles, artists)]
# print(song_list)

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
print(client_id)
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
print(client_secret)

redirect_uri = "http://example.com"
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                               client_secret=client_secret, 
                                               redirect_uri=redirect_uri, 
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path='token.txt'))

user_id = sp.current_user()['id']
playlist_name = f"Billboard Hot 100 on {date_input}"
playlist_description = f"A playlist that includes song from the Billboard Hot 100 on {date_input}"

# Create a new playlist
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
print(f"Playlist {playlist_name} is created successfully! The playlist_id is {new_playlist['id']}.")

# Define function to search for a song
def search_song(song_name):
    result = sp.search(q=song_name, limit=1, type='track', market='US')
    if result['tracks']['items']:
        return result['tracks']['items'][0]['uri']
    return None
    
# Add songs to the playlist
song_uris = []

for song in song_list:
    song_searched = search_song(song)
    if song_searched:
        song_uris.append(song_searched)
        print(f"Found song: {song}")
    else:
        print(f"Could not find song: {song}")
        
if song_uris:
    sp.playlist_add_items(playlist_id=new_playlist['id'], items=song_uris)
    print(f"Added {len(song_uris)} songs to the playlist!")
else:
    print(f"No songs were found and added.")