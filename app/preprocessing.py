def preprocess_data(input_data):
    """
    Preprocess the input data for model inference.
    Example: Normalize, tokenize, or transform input as required by the model.
    """
    if isinstance(input_data, str):
        return input_data.lower()
    elif isinstance(input_data, dict):
        return {key: str(value).lower() for key, value in input_data.items()}
    else:
        raise ValueError("Unsupported data format for preprocessing")
