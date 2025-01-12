#### Application Logging
```
from app.logger import app_logger
app_logger.info("Application started successfully")
```

#### Module(s) Logging
```
from app.logger import get_logger
model1_logger = get_logger("model1")
model1_logger.info("Model 1 prediction started")
```

### Running application
$ quart run

## Project Structure
```
ML-Bkd
├── app
│   ├── config
│   │   └── __init__.py
│   ├── logger.py
│   ├── logs
│   │   └── app.log
│   ├── main.py
│   ├── middleware
│   │   └── rateLimiter.py
│   ├── middlewares.py
│   ├── models
│   │   ├── encoded_user_data.pkl
│   │   ├── label_encoders.pkl
│   │   └── scalers.pkl
│   ├── models.py
│   ├── preprocessing.py
│   ├── routes.py
│   ├── services
│   │   ├── __init__.py
│   │   └── prediction_service.py
│   ├── utils
│   │   └── reponse.py
│   └── utils.py
├── Dockerfile
├── logs
│   └── app.log
├── README.md
└── requirements.txt
```