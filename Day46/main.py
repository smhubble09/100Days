import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "ID"
CLIENT_SECRET = "SECRET"
OAUTH_REDORECT_URI = "https://example.com/callback"

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
#Scrape data from website
url = f"https://www.billboard.com/charts/hot-100/{travel_date}/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

#List of songs
all_songs = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_names = [song.text.strip() for song in all_songs]

song_uris = []
year = travel_date.split("-")[0]
#Spotify connection
auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=OAUTH_REDORECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="Day46/token.txt")
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
#Search for songs
for song in song_names:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query,type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skpped.")

#Create playlist
playlist = sp.user_playlist_create(user=user_id,name=f"{travel_date} Billboard 100",public=False,collaborative=False,description="Playlist created via Python")
#Add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
