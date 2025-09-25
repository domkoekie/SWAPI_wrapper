from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

auth_bp = Blueprint("auth", __name__) #blueprint for routes

def init_jwt(app):
    app.config["JWT_SECRET_KEY"] = "ilovesenwes"
    jwt = JWTManager(app)
    return jwt

#POST /login endpoint
@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "katelyn" or password != "swapi": #hardcoded authentication values
        return jsonify({"error": "Invalid credentials"}), 401 #error handling

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200 #successful request returning JWT token
