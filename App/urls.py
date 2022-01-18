from django.urls import path
from . import views

app_name = 'App'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Авторизация пройдена
    path('user', views.user, name='user'),  
    path('top_genres', views.top_genres),  
    path('create_playlist', views.create_playlist)
]