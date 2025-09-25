from flask import Flask, jsonify
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from swapi_service import get_films, get_film_characters, get_film_starships
from authentication import auth_bp, init_jwt
app = Flask(__name__)

jwt = init_jwt(app)

app.register_blueprint(auth_bp)

# Create Limiter without app
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

# Attach Limiter to app
limiter.init_app(app)

@app.route("/films")
@limiter.limit("10 per minute")
@jwt_required()
def films():
    return jsonify(get_films()), 200

@app.route("/films/<int:film_id>/characters")
@limiter.limit("5 per minute")
@jwt_required()
def characters(film_id):
    chars = get_film_characters(film_id)
    if chars is None:
        return jsonify({"error": "Film not found"}), 404
    return jsonify(chars), 200

@app.route("/films/<int:film_id>/starships")
@limiter.limit("5 per minute")
@jwt_required()
def starships(film_id):
    ships = get_film_starships(film_id)
    if ships is None:
        return jsonify({"error": "Film not found"}), 404
    return jsonify(ships), 200

if __name__ == "__main__":
    app.run(debug=True)
