from app.logger import app_logger
app_logger.info("Application started successfully")


from app.logger import get_logger
model1_logger = get_logger("model1")
model1_logger.info("Model 1 prediction started")


## Running application (TESTING)
export FLASK_APP=app.main
export FLASK_ENV=development
flask run


## Production Mode
For production, use a WSGI server like gunicorn:
$ gunicorn -w 4 -b 0.0.0.0:5000 app.main:app


## Project Structure
project/
│
├── app/                           # Core application directory
│   ├── __init__.py                # Makes `app` a package, initializes the app
│   ├── main.py                    # Entry point to run the app
│   ├── logger.py                  # Logger configuration
│   ├── routes.py                  # Flask routes for the app
│   ├── models/                    # Directory for ML models and logic
│   │   ├── __init__.py            # Makes `models` a package
│   │   ├── model1.py              # Model 1 logic
│   │   ├── model2.py              # Model 2 logic
│   ├── middleware/                # Directory for middleware logic
│   │   ├── __init__.py            # Makes `middleware` a package
│   │   ├── auth.py                # Authentication middleware
│   │   ├── validation.py          # Input validation middleware
│   ├── preprocessing/             # Directory for preprocessing logic
│   │   ├── __init__.py            # Makes `preprocessing` a package
│   │   ├── utils.py               # Preprocessing helper functions
│
├── config/                        # App configuration
│   ├── __init__.py                # Makes `config` a package
│   ├── config.py                  # Configurations for app/environment
│
├── logs/                          # Directory for log files
│   ├── app.log                    # General app logs
│   ├── model1.log                 # Logs specific to model1
│   ├── model2.log                 # Logs specific to model2
│
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
├── README.md                      # Documentation
