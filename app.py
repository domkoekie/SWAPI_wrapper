from flask import Flask, jsonify
from swapi_service import get_films, get_film_characters, get_film_starships

app = Flask(__name__)

@app.route("/films", methods=["GET"])
def films():
    return jsonify(get_films()), 200

@app.route("/films/<int:film_id>/characters", methods=["GET"])
def characters(film_id):
    characters = get_film_characters(film_id)
    if characters is None:
        return jsonify({"error": "Film not found"}), 404
    return jsonify(characters), 200

@app.route("/films/<int:film_id>/starships", methods=["GET"])
def starships(film_id):
    starships = get_film_starships(film_id)
    if starships is None:
        return jsonify({"error": "Film not found"}), 404
    return jsonify(starships), 200

if __name__ == "__main__":
    app.run(debug=True)
