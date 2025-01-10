from quart import request, jsonify
from functools import wraps
from app.config import Config
import os

def auth_middleware(func):
    """
    Middleware to check for authentication token in the headers.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {Config.SECRET_KEY}":
            return jsonify({"error": "Unauthorized"}), 401
        return await func(*args, **kwargs)
    return wrapper
