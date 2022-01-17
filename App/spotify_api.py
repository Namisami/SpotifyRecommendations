import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SP():
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="df8949840c764e07999105485f556f82",
                                                client_secret="173a06da9b794b199a76632cf290b0eb",
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-library-read user-top-read"))
    def sp_login(self):
        sp = self.sp.current_user()
        username = sp['display_name']
        userpic = sp['images'][0]['url']
        context = {'username': username, 'userpic': userpic}
        return context
    def sp_top_genres(self):
        artists = self.sp.current_user_top_artists()
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])