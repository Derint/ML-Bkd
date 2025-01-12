from quart import Blueprint, request, jsonify
from app.middlewares import auth_middleware
from app.services.prediction_service import recommendUsers
from app.middleware.rateLimiter import rate_limiter


routes = Blueprint("routes", __name__)


@routes.route("/recommend-user/<userId>", methods=["POST"])
# @auth_middleware
async def predict(userId):
    """
    Route to handle predictions from a specific model.
    """

    data = await request.get_json()
    print("\n\nDATA::", data)
    response, status_code = await recommendUsers(userId, data)
    return jsonify(response), status_code


@routes.route("/health", methods=["GET"])
async def health_check():
    """
    Health check endpoint.
    """
    return jsonify({"status": "Healthy"}), 200


@routes.route("/favicon.ico")
async def favicon():
    return jsonify({}), 204
