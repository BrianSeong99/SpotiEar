import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

MBTI_indexes = {
    "INTJ": 0,
    "INTP": 1,
    "ENTJ": 2,
    "ENTP": 3,

    "INFJ": 4,
    "INFP": 5,
    "ENFJ": 6,
    "ENFP": 7,

    "ISTJ": 8,
    "ISFJ": 9,
    "ESTJ": 10,
    "ESFJ": 11,

    "ISTP": 12,
    "ISFP": 13,
    "ESTP": 14,
    "ESFP": 15,
}

# reference: https://open.spotify.com/user/pq8w5snqhyu97x4x4kmsmaxup/playlists
my_playlist = [
  ['37i9dQZF1E8LXKtwXNYMj6'], # brian
  ['37i9dQZF1E8O6v2Ugx4bKy'], # brian
  # ['6m8yMqUVIf68BdLS0bAVtf'], # anqi
  # ['6mgWUWQhvRnkuxUZaE96vZ'], # anqi
  # ["37i9dQZF1DXbehaqJzJXqw"], # anqi
  # ['37i9dQZF1EQpz3DZCEoX3g'], # anqi
]
csv = open("data/data_brian.csv", "w")

arr = []
data_size = 0
for playlist in my_playlist:
  for playlist_uri in playlist:
    time.sleep(1)
    response = sp.playlist(playlist_uri)
    songs_in_playlist = response["tracks"]["items"]
    id_arr = [ele["track"]["id"] for ele in songs_in_playlist]
    features = sp.audio_features(id_arr)
    data_size = data_size + len(features)
    print(data_size)
    for feature in features:
      arr.append(
        str(feature["acousticness"]) + ',' 
        + str(feature["danceability"]) + ',' 
        + str(feature["energy"]) + ',' 
        + str(feature["instrumentalness"]) + ',' 
        + str(feature["key"]) + ',' 
        + str(feature["liveness"]) + ',' 
        + str(feature["loudness"]) + ',' 
        + str(feature["speechiness"]) + ',' 
        + str(feature["tempo"]) + ',' 
        + str(feature["time_signature"]) + ',' 
        + str(feature["valence"]) + ',' 
        + str(2) + '\n'
      )

csv.write("acousticness,danceability,energy,instrumentalness,key,liveness,loudness,speechiness,tempo,time_signature,valence,mbti\n")
for record in arr:
  csv.write(record)

# with open("data.txt", "w") as f:
#   print(data)
#   f.write(str(data))

# print(sp.audio_features("3CnUGF7phvydXWBJUBDDP6")[0])