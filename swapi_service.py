import requests
from cache import Cache

BASE_URL = "https://swapi.dev/api"
cache = Cache(ttl=300)

def fetch_data(url):
    cached = cache.get(url)
    if cached:
        return cached

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cache.set(url, data)
        return data
    else:
        return None

def get_films():
    data = fetch_data(f"{BASE_URL}/films/")
    return data.get("results", []) if data else []

def get_film_characters(film_id):
    film = fetch_data(f"{BASE_URL}/films/{film_id}/")
    if not film:
        return None
    return [fetch_data(url).get("name") for url in film.get("characters", [])]

def get_film_starships(film_id):
    film = fetch_data(f"{BASE_URL}/films/{film_id}/")
    if not film:
        return None
    return [fetch_data(url).get("name") for url in film.get("starships", [])]
