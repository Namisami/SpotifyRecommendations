from cgi import print_form
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fe12c6c204fd45a181110cc2f8495441",
                                               client_secret="529eb299171d43689205e3da3806c864",
                                               redirect_uri="https://example.com/callback/",
                                               scope="user-library-read"))

print(sp.current_user())
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])