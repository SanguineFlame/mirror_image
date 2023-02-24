import spotipy
import secrets
from spotipy.oauth2 import SpotifyOAuth
import collections
import json
import pandas
import sqlite3

conn = sqlite3.connect('python_spotify.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Genres(genre_tally, TEXT, Tally Integer)''')

sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.client_id, client_secret=secrets.client_secret,
                                                   redirect_uri=secrets.redirect_uri,
                                                   scope='user-read-recently-played'))

recently_played = sp_obj.current_user_recently_played(limit=50)

# print(json.dumps(recently_played, indent=4, sort_keys=True))

artist_id = ''
collection_of_genres = []
for item in recently_played['items']:
    artist_id = item['track']['album']['artists'][0]['id']
    collection_of_genres.extend(sp_obj.artist(artist_id)['genres'])

tally = collections.Counter()
for genre in collection_of_genres:
    tally[genre] += 1

genre_df = pandas.DataFrame(list(tally.items()), columns=['Genre', 'Tally'])
genre_df.to_sql(name='genre_tally', con=conn, if_exists='replace', index=False)


