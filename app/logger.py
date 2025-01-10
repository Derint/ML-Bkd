import logging
from logging.handlers import RotatingFileHandler
import json, os

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


# JSON Formatter for structured logs
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


def setup_general_logger():
    """
    Setup advanced logging configuration for the entire app.
    """
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)

    # Console handler (development)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Change to DEBUG for more verbose logs
    file_formatter = JSONFormatter()
    console_handler.setFormatter(file_formatter)  # Use JSONFormatter for console as well

    # File handler with rotation
    file_handler = RotatingFileHandler(
        f"{log_dir}/app.log", maxBytes=5 * 1024 * 1024, backupCount=3  # 5 MB per file
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Setup for the general logger
app_logger = setup_general_logger()
app_logger.info("Logger is set up correctly!")

# Function to get module-specific loggers
def get_logger(module_name):
    """
    Get a logger specific to the module.
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # File handler for module-specific logs
    file_handler = RotatingFileHandler(
        f"{log_dir}/{module_name}.log", maxBytes=5 * 1024 * 1024, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)

    # Console handler for development
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Change to DEBUG for more verbose logs

    # Formatter for both handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.handlers:  # Avoid duplicate handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
