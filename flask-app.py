from flask import Flask, jsonify
import csv

all_movies = []
liked_movies = []
unliked_movies = []
not_watched_movies = []

with open('movies.csv', 'r', encoding = "utf_8") as f:
    reader = csv.reader(f)
    movie_data = list(reader)
    all_movies = movie_data[1:]

app = Flask(__name__)

@app.route('/get_movie')
def get_movie():
    return jsonify({
        'data': all_movies[0],
        'status': 'succesful'
    }), 404

@app.route('/liked_movies', methods = ['POST'])
def like_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status': 'success'
    }), 404

@app.route('/unliked_movies', methods = ['POST'])
def unlike_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        'status': 'success'
    }), 404

@app.route('/not_watched_movies', methods = ['POST'])
def not_watch_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        'status': 'success'
    }), 404


if __name__ == "__main__":
  app.run()