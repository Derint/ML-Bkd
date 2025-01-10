from app.models import PredictionInput
from quart import jsonify
from pydantic import ValidationError
import joblib
import os


async def validate_input(data):
    """
    Validate input data using Pydantic.
    """
    try:
        validated_data = PredictionInput.model_validate(data)
        return validated_data.input, None
    except ValidationError as e:
        return None, e.errors()


async def perform_prediction(model_func, input_data):
    """
    Perform asynchronous prediction.
    """
    import asyncio
    await asyncio.sleep(0.1)  # Simulate async operation
    return model_func(input_data)


def create_response(data=None, status_code=200, message="success"):
    """
    General function to create a JSON response.

    Args:
        data (dict, optional): Data to be included in the response body.
        status_code (int, optional): HTTP status code for the response.
        message (str, optional): A custom message to include in the response.

    Returns:
        Response: Quart Response object with status code and data.
    """
    # Check if the status code is in the 2xx range (success)
    # if 200 <= status_code < 300:
    #     status = "success"
    # else:
    #     status = "error"

    response_data = {
        "code": status_code,
        "message": message or "",  
        "data": data or {},        
    }
    
    return response_data, status_code


def loadPickelModel(filepath):
    if not os.path.exists(filepath):
        return False, "Model Path does not exits"
    model = joblib.load(filepath)
    return True, model