from django.urls import path

from . import views

app_name = 'App'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Авторизация пройдена
    path('user/', views.user, name='user'),
]