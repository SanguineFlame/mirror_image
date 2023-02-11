import spotipy
import secrets
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
import json
import rich

scope = 'user-read-recently-played'

sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.client_id, client_secret=secrets.client_secret,
                                                   redirect_uri=secrets.redirect_uri, scope=scope))

recently_played = sp_obj.current_user_recently_played(limit=1)

rich.print(recently_played)
# print(json.dumps(recently_played, indent=4, sort_keys=True))


# for item in recently_played['items']:
#     print(item['track']['album']['artists'][0]['name'])
#
# for item in recently_played['items']:
#     print(item['track']['name'])
