from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def index(request):
    return render(request, 'App/index.html')

def user(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fe12c6c204fd45a181110cc2f8495441",
                                               client_secret="529eb299171d43689205e3da3806c864",
                                               redirect_uri="https://example.com/callback/",
                                               scope="user-library-read"))
    sp = sp.current_user()
    username = sp['display_name']
    userpic = sp['images'][0]['url']
    context = {'username': username, 'userpic': userpic}
    return render(request, 'App/user.html', context)
