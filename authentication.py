from flask import request, jsonify

API_KEY = "ilovesenwes"

def require_api_key(func):
    def wrapper(*args, **kwargs):
        key = request.headers.get("Authorization")
        if key == f"Bearer {API_KEY}":
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized user"}), 401
    wrapper.__name__ = func.__name__
    return wrapper