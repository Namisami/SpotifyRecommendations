import spotipy
from spotipy.oauth2 import SpotifyOAuth

from App import constants

class SP():
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="df8949840c764e07999105485f556f82",
                                                client_secret="173a06da9b794b199a76632cf290b0eb",
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-library-read user-top-read playlist-modify-private playlist-modify-public"))

    def sp_login(self):
        sp = self.sp.current_user()
        username = sp['display_name']
        #Проверка на случай, если у пользователя нет фото
        try:
            userpic = sp['images'][0]['url']
        except IndexError:
            userpic = 'https://sun9-37.userapi.com/impg/IMCW-A_pG3CK2HYiv_va5tELmOEyjXslJZTNaQ/OxtzI64Kqls.jpg?size=1000x1000&quality=96&sign=384f9969835bcaceaec6a02c48b397c4&type=album'
        context = {'username': username, 'userpic': userpic}
        return context

    def sp_top_genres(self):
        # Топ жанры
        try:
            try:
                genres_dict = self.top_genres_collect()
                self.reccomendations(", ".join(list(genres_dict.values())))
                return genres_dict
            except SpotifyException:
                pass
        except NameError:
            pass

    def top_genres_count(self, results):
        # Подсчет всех жанров которые есть и их сортировка
        genres = set()
        genres_dict = {}
        for item in (results['items']):
            for genre in item['genres']:
                if genre not in genres:
                    genres.add(genre)
                    genres_dict[genre] = 1
                else:
                    genres_dict[genre] += 1
        return (sorted(genres_dict.items(), key = lambda item: item[1], reverse=True)[:4])

    def top_genres_collect(self):
        # Вынос общего
        results = self.sp.current_user_top_artists(time_range=constants.TIME_RANGE, limit=constants.ARTISTS_NUMBER)
        genres_dict = {}
        for i, genre in enumerate(self.top_genres_count(results)):
            genres_dict[f'genre{i + 1}'] = genre[0]
        return genres_dict

    def reccomendations(self, genres):
        track_urls = []
        genres_arr = genres.split(", ")
        # results - огромный словарь данных. Для поиска нужного сперва вводи print(results) а дальше ищи в нем нужную пару ключ: значение
        results = self.sp.recommendations(seed_genres=genres_arr, limit=constants.TRACKS_NUMBER)
        for result in results['tracks']:
            track_url = result['external_urls']['spotify']
            track_urls.append(track_url)
        
        return track_urls

    def create_playlist(self):
        user_me = self.sp.me()
        all_playlists = self.sp.current_user_playlists(limit=50)
        for i in range(len(all_playlists['items'])):
            if str(all_playlists['items'][i]['name'])==constants.PLAYLIST_NAME:
                self.sp.current_user_unfollow_playlist(all_playlists['items'][i]['id'])
        self.sp.user_playlist_create(user_me['id'] , constants.PLAYLIST_NAME, public=True, collaborative=False, description='')
        self.add_songs()

    def receive_playlist(self):
        playlist = self.sp.current_user_playlists(limit=1, offset=0)
        return playlist

    def add_songs(self):
        # Добавляет песни в плейлист
        genres_dict = self.top_genres_collect()
        playlist = self.sp.current_user_playlists(limit=1, offset=0)
        playlist_id = playlist['items'][0]['id']
        tracks = (", ".join(list(genres_dict.values())))
        tracks = self.reccomendations(tracks)
        self.sp.playlist_add_items(playlist_id, tracks)

    def first_songs(self):
        playlist = self.receive_playlist()
        playlist_id = playlist['items'][0]['id']
        response = self.sp.playlist_items(playlist_id,
                                 offset=0,
                                 limit = 6,
                                 fields='',
                                 additional_types=['track'])
        track_list = {}
        for i, composition in enumerate(response['items']):
            artist = composition['track']['artists'][0]['name']
            track = composition['track']['name']
            track_list[f'artist{i + 1}'] = artist
            track_list[f'track{i + 1}'] = track
        return track_list

    def receive_playlist_link(self):
        playlist = self.receive_playlist()
        playlist_link = playlist['items'][0]['external_urls']['spotify']
        return {'playlist_link': playlist_link}
