from django.shortcuts import render

from App import cache_clean, spotify_api

def index(request):
    cache_clean.cache_clean()
    return render(request, 'App/index.html', { user: 'user'})

def user(request):
    context = spotify_api.sp_login()
    return render(request, 'App/user.html', context)
