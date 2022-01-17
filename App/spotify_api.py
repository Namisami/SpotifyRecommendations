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
        # Топ жанры
        sp_range = 'medium_term'
        results = self.sp.current_user_top_artists(time_range=sp_range, limit=50)
        
        genres_dict = {}
        for i, genre in enumerate(self.top_genres_count(results)):
            genres_dict[f'genre{i + 1}'] = genre[0]
        self.reccomendations(", ".join(list(genres_dict.values())))
        return genres_dict

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
    
    #Просто конвертирует строку в список
    def genres_failure_protection(self, string):
        arr = []
        text = ''
        skip = False
        k = 0
        for i in string:
            k+=1
            if skip == True:
                skip = False
                
            elif i == ',':
                arr.append(text)
                text = ''
                skip = True
            elif k==len(string):
                text+=i
                arr.append(text)
            else:
                text += i
        return arr

    def reccomendations(self, genres):
        genres_arr = self.genres_failure_protection(genres)

        # results - огромный словарь данных. Для поиска нужного сперва вводи print(results) а дальше ищи в нем нужную пару ключ: значение
        results = self.sp.recommendations(seed_genres=genres_arr, limit=1)
        print(results['tracks'][0]['artists'][0]['name'])
        print('---------------')
        print(results['tracks'][0]['name'])

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])