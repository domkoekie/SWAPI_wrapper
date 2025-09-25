from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

auth_bp = Blueprint("auth", __name__)

def init_jwt(app):
    app.config["JWT_SECRET_KEY"] = "ilovesenwes"
    jwt = JWTManager(app)
    return jwt

# Login endpoint
@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Simple hardcoded check (replace with DB or service in real life)
    if username != "katelyn" or password != "swapi":
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
