from dotenv import load_dotenv
from quart import Quart, request, jsonify
from app.config import Config
from app.routes import routes
from app.logger import app_logger
from app.middleware.rateLimiter import rate_limiter
import asyncio, atexit, signal

load_dotenv()

def create_app():
    """
    Factory to create and configure the Quart app.
    """
    app = Quart(__name__)
    app.config.from_object(Config)

    # Log when the app is created
    app_logger.info("Creating the application")

    # Register blueprints
    print("APP_PREFIX::", Config.APP_PREFIX)
    app.register_blueprint(routes, url_prefix=Config.APP_PREFIX + '/api/v1')

    app_logger.info("Routes registered successfully")

    @app.before_request
    async def check_rate_limit():
        if app.config["MODE"]!='development':  
            ip = request.remote_addr 
            if not rate_limiter.check_rate_limit(ip):
                return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

    
    return app


def shutdown(signal_received, frame):
    """
    Graceful shutdown function. Handles cleanup tasks before quitting the app.
    """
    app_logger.info("Gracefully shutting down the application...")
    asyncio.create_task(app.shutdown())  # Shutdown async tasks if any
    exit(0)


app = create_app()

app_logger.info("Starting Application")
app_logger.info(f"Debug mode: {app.config['DEBUG']}")


# Register signal handlers for SIGINT and SIGTERM (Ctrl+C and terminate signal)
signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

# Register cleanup actions to run on shutdown
atexit.register(lambda: app_logger.info("Application is shutting down"))


app.run(
    host=app.config["HOST"], 
    port=app.config["PORT"],
    debug=app.config["DEBUG"]
)
