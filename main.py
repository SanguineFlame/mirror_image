import spotipy
import secrets
from spotipy.oauth2 import SpotifyOAuth
import collections
import json
import pandas

scope = 'user-read-recently-played'

sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.client_id, client_secret=secrets.client_secret,
                                                   redirect_uri=secrets.redirect_uri, scope=scope))

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

genre_df = pandas.DataFrame.from_dict(tally, orient='index', columns=['Genre Tally'])
print(genre_df.to_string())

