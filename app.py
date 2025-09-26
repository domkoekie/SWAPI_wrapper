from flask import Flask, jsonify
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from swapi_service import get_films, get_film_characters, get_film_starships
from authentication import auth_bp, init_jwt
import os
app = Flask(__name__)
jwt = init_jwt(app)
app.register_blueprint(auth_bp)

#rate limiter initialization
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"] #default rate limit
)

limiter.init_app(app)


#GET /films endpoint
@app.route("/films")
@limiter.limit("10 per minute")  #rate limit to 10 requests per minute
@jwt_required()
def films():
    return jsonify(get_films()), 200 #successful request


#GET /films/{id}/characters endpoint
@app.route("/films/<int:film_id>/characters")
@limiter.limit("5 per minute")  #rate limit to 5 requests per minute
@jwt_required()
def characters(film_id):
    chars = get_film_characters(film_id)
    if chars is None:
        return jsonify({"error": "Film not found"}), 404  #error handling
    return jsonify(chars), 200 #successful request


#GET /films/{id}/starships endpoint
@app.route("/films/<int:film_id>/starships")
@limiter.limit("5 per minute")  #rate limit to 5 requests per minute
@jwt_required()
def starships(film_id):
    ships = get_film_starships(film_id)
    if ships is None:
        return jsonify({"error": "Film not found"}), 404  #error handling
    return jsonify(ships), 200 #successful request


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  #Heroku port or local
    app.run(host="0.0.0.0", port=port, debug=True)
