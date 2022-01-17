import os
def cache_clean():
    # Удаляет .cache, если он есть перед тем, как отрисовать окно index.html
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../.cache')
        os.remove(path)
    except FileNotFoundError:
        pass