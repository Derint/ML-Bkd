import os, signal
from dotenv import load_dotenv
from pathlib import Path

# Get the base directory (project root)
CONFIG_DIR = Path(__file__).resolve().parent

# Navigate to the app directory (parent of config/)
APP_DIR = CONFIG_DIR.parent

# Navigate to the models directory
MODELS_DIR = APP_DIR / "models"

print(f"Model Directory: {MODELS_DIR}")
if not MODELS_DIR.exists():
    print(f"Error: The required directory '{MODELS_DIR}' does not exist.")
    os.kill(os.getpid(), signal.SIGTERM)

load_dotenv()

class Config:
    MODE = os.getenv("MODE", 'development')
    APP_PREFIX = os.getenv("APP_PREFIX", "/api")
    SECRET_KEY = os.getenv("SECRET_KEY", "sample-key-over-here")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 4000))

    DEBUG = MODE=='development' # os.getenv("DEBUG", False)


class ModelConfig:
    ENCODER_PATH = os.path.join(MODELS_DIR, 'encoded_user_data.pkl')
  

