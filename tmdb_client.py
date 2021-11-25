import requests
import json
import os

#API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZGEzYzhhYmEyODVhZDBhZjYxM2E5NmEyMWZlMDllNiIsInN1YiI6IjYwMmQzNWVhZDRiOWQ5MDAzZmQyOWY1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oDchyvN4gbwaNHGH2QsEs2mJiUGJStE76Rvby3CY3kU"


def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   return response.json()


# TOP RATED MOVIES
# def get_top_rated_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/top_rated"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def get_top_rated_movies():
    return call_tmdb_api(f"movie/top_rated")

# UPCOMING MOVIES
# def get_upcoming_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/upcoming"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()   

def get_upcoming_movies():
    return call_tmdb_api(f"movie/upcoming")

# POPULAR MOVIES
# def get_popular_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/popular"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def get_popular_movies():
    return call_tmdb_api(f"movie/popular")

 # MOVIES NOW PLAYING
# def get_now_playing_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/now_playing"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()  

def get_now_playing_movies():
    return call_tmdb_api(f"movie/now_playing")

# MOVIE DETAILS    
# def get_single_movie(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_movies(how_many, list_type):
    if list_type == "popular":
        data = get_popular_movies()
    elif list_type =="top_rated":
        data = get_top_rated_movies()
    elif list_type == "upcoming":
        data = get_upcoming_movies()
    elif list_type == "now_playing":
        data = get_now_playing_movies()
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

# def get_single_movie_cast(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()["cast"]

def get_single_movie_cast(movie_id, how_many=12):
    data = call_tmdb_api(f"movie/{movie_id}/credits")
    return data['cast'][:how_many]

# def get_movie_images(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()["cast"]

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


# def get_movies_list(list_type):
#     endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     response.raise_for_status()
#     return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_airing_today():
    return call_tmdb_api(f"tv/airing_today")["results"]


def search(search_query):
    return call_tmdb_api(f"search/movie/?query={search_query}")["results"]