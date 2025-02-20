import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import time
import os

pp = pprint.PrettyPrinter(indent=0)

client_ID = os.environ["client_ID"]
client_secret = os.environ["client_secret"]
scope = "playlist-modify-public"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_ID,
        client_secret=client_secret,
        redirect_uri="http://mysite.com/callback/",
        scope=scope,
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

date = input("What year would you like to create a spotify playlist (please use the YYYY-MM-DD format): ")

while len(date) != 10:
    print("please use correct date format YYYY-MM-DD")
    date = input("What year would you like to create a spotify playlist (please use the YYYY-MM-DD format): ")

year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]

print("Creating spotify playlist...")
time.sleep(1)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website = response.text

soup = BeautifulSoup(website, "html.parser")
titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
artists = soup.find_all(name="span", class_="a-font-primary-s")

t100_list = [title.getText().strip("\n\t") for title in titles]

t100_artist = [artist.getText().strip("\n\t") for artist in artists]

for artist in t100_artist:
    if artist == "RIAA Certification:":
        t100_artist.remove(artist)

song_uris = []

artist_index_count = 0
for tracks in t100_list:
    results = sp.search(q=f"track:{tracks} artist: {t100_artist[artist_index_count]}", type="track")
    artist_index_count += 1
    try:
        song_uri = results["tracks"]["items"][0]["uri"]
        print(song_uri)
        song_uris.append(song_uri)
    except IndexError:
        print("Track number " + str(t100_list.index(tracks) + 1) + " cannot be found")

playlists = sp.user_playlist_create(user=f"{user_id}", name=f"{year} Billboard top 100 ({day}/{month})", public=True, description=f"Top Tracks from the year: {year}")

sp.playlist_add_items(playlist_id=playlists["id"], items=song_uris)

print(f"\n...Your playlist has been created, we managed to find a total of {len(song_uris)}/100 of the top 100 songs! ")
