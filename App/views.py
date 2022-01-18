from django.shortcuts import render

from App import cache_clean, spotify_api

def index(request):
    cache_clean.cache_clean()
    return render(request, 'App/index.html', { user: 'user'})

def user(request):
    sp = spotify_api.SP()
    top_genres = sp.sp_top_genres()
    login = sp.sp_login()
    context = {**login, **top_genres}
    sp.create_playlist()
    return render(request, 'App/user.html', context)
