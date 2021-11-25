
from flask import Flask, render_template, url_for, request, redirect, flash
import tmdb_client
import random
import datetime


app = Flask(__name__)

FAVORITES = set()

@app.route('/')
def homepage():
    available_lists = ['now_playing', 'popular', 'top_rated', 'upcoming']
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in available_lists:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    for movie in movies:
        random.shuffle(movies)
    return render_template("homepage.html", movies=movies, current_list=selected_list, available_lists=available_lists)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}



@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=movie, cast=cast, selected_backdrop=selected_backdrop)


@app.route('/search')
def search():
    search_query = request.args.get("q","")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)


@app.route('/today')
def today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("today.html", movies=movies, today=today)




@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if request.method == "POST":
        if movie_id not in FAVORITES:
            FAVORITES.add(movie_id)
            flash(f"Dodano {movie_title} do ulubionych!")
        else:
            flash(f" {movie_title} już jest w ulubionych!")
        return redirect(url_for("homepage"))
    



@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("favorites.html", favorites=FAVORITES, movies=movies)


app.secret_key = b'gombao'
if __name__ == '__main__':
    app.run(debug=True)