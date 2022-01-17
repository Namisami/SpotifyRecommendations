from django.shortcuts import render

from App import cache_clean, spotify_api

def index(request):
    cache_clean.cache_clean()
    return render(request, 'App/index.html', { user: 'user'})

def user(request):
    sp = spotify_api.SP()
    context = sp.sp_login()
    return render(request, 'App/user.html', context)
