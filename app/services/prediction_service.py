from app.utils import validate_input, perform_prediction
from app.preprocessing import preprocess_data
from app.utils import create_response
from sklearn.metrics.pairwise import cosine_similarity
from app.config import ModelConfig
from http import HTTPStatus
from quart import jsonify, Response
from app.utils import loadPickelModel
import pandas as pd


RECOMMED_USER_MODEL = None

FEATURES = [
    {'name': 'country', 'type': 'categorical'},  # Categorical feature
    {'name': 'designation', 'type': 'categorical'}, 
    {'name': 'course', 'type': 'categorical'},  
    {'name': 'subjects', 'type': 'categorical'},  
    # {'name': 'age', 'type': 'numerical'},  # Numerical feature
]


def getRecommedUserModel():
    global RECOMMED_USER_MODEL
    if RECOMMED_USER_MODEL is None:
        ok, RECOMMED_USER_MODEL = loadPickelModel(ModelConfig.ENCODER_PATH)
        if ok:
            RECOMMED_USER_MODEL = pd.DataFrame(RECOMMED_USER_MODEL)
    return RECOMMED_USER_MODEL


def compute_similarities(user_data, user_id, features):
    # Extract feature vectors for all users
    feature_columns = [feature['name'] for feature in features]
    # print("\n\n==>>feature_columns::", feature_columns, type(user_data))
    user_features = user_data[feature_columns]
    
    # Find the index of the given user
    user_index = user_data[user_data['_id'] == user_id].index[0]
    
    # Compute cosine similarities between the target user and all others
    similarities = cosine_similarity(user_features.iloc[user_index].values.reshape(1, -1), user_features)
    
    return similarities[0]


def get_most_similar_users(user_data, user_id, features, top_n=5):
    similarities = compute_similarities(user_data, user_id, features)

    # Sort by similarity and get the top n users (excluding the target user itself)
    similar_users_idx = similarities.argsort()[::-1][1:top_n+1]
    similar_users = user_data.iloc[similar_users_idx]["_id"].tolist()
    
    return similar_users # similar_users


async def recommendUsers( userId ):
    """
    Handles the prediction request by validating input, preprocessing, and calling the model.
    """
   
    # Validate input
    # input_data, errors = await validate_input(userId)
    # if errors:
    #     return {"error": errors}, 400

    try:
        # Preprocess input
        # preprocessed_data = preprocess_data(input_data)

        # Perform prediction
        # prediction = await perform_prediction(models[model_name], preprocessed_data)
        # Some logic to generate response data
        # data = {"user_id": userId, "recommendations": "sample recommendations"}
        encoded_data = getRecommedUserModel()

        if encoded_data[encoded_data['_id']==userId].shape[0] == 0:
            print("-->userId", userId)
            return create_response([], HTTPStatus.NOT_FOUND, "user data not found")
        # print(encoded_data.info())
        similar_users = get_most_similar_users(encoded_data, userId, FEATURES)
        print("\n\n===>>similar_users::", similar_users)
        return create_response(similar_users, HTTPStatus.OK)
        # return response_data, status_code
        
        # response_data, status_code = 
        # return jsonify(response_data), 200

    except ValueError as e:
        return {"error": f"Preprocessing error: {str(e)}"}, 400
    except Exception as e:
        print(e)
        return {"error": f"An error occurred: {str(e)}"}, 500
