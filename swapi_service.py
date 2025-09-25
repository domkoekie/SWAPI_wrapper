import requests
from cache import Cache

BASE_URL = "https://swapi.dev/api" #base url for SWAPI
cache = Cache(ttl=300)

def fetch_data(url): #data from cache
    cached = cache.get(url)
    if cached:
        return cached

#if cache is empty get from API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cache.set(url, data) #store data in cache if successful request
        return data
    else:
        return None

#returns all films
def get_films():
    data = fetch_data(f"{BASE_URL}/films/")
    return data.get("results", []) if data else []

#returns characters for specified film
def get_film_characters(film_id):
    film = fetch_data(f"{BASE_URL}/films/{film_id}/")
    if not film:
        return None
    return [fetch_data(url).get("name") for url in film.get("characters", [])]

#returns starships for specified film
def get_film_starships(film_id):
    film = fetch_data(f"{BASE_URL}/films/{film_id}/")
    if not film:
        return None
    return [fetch_data(url).get("name") for url in film.get("starships", [])]
