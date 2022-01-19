from django.shortcuts import render

from App import cache_clean, spotify_api

def index(request):
    cache_clean.cache_clean()
    return render(request, 'App/index.html')

def user(request):
    sp = spotify_api.SP()
    login = sp.sp_login()
    context = login
    return render(request, 'App/user.html', context)

def top_genres(request):
    sp = spotify_api.SP()
    login = sp.sp_login()
    top_genres = sp.sp_top_genres()
    context = {**login, **top_genres}
    print(context)
    return render(request, 'App/top_genres.html', context)

def create_playlist(request):
    sp = spotify_api.SP()
    sp.create_playlist()
    login = sp.sp_login()
    top_genres = sp.sp_top_genres()
    context = {**login, **top_genres}
    return render(request, 'App/create_playlist.html', context)