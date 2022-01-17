from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def index(request):
    # Удаляет .cache, если он есть перед тем, как отрисовать окно index.html
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../.cache')
        os.remove(path)
    except FileNotFoundError:
        pass

    return render(request, 'App/index.html', { user: 'user'})

def user(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="df8949840c764e07999105485f556f82",
                                               client_secret="173a06da9b794b199a76632cf290b0eb",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))
    sp = sp.current_user()
    username = sp['display_name']
    userpic = sp['images'][0]['url']
    context = {'username': username, 'userpic': userpic}
    return render(request, 'App/user.html', context)
