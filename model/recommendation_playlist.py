import pandas as pd
import numpy as np
from pandas import DataFrame
import pickle
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=FutureWarning)

data = pd.read_csv('data/train_data.csv')

def get_pourcentage_movement(count_movement: int, total_movement: int, count_not_movement: int) -> float | int:
    returned_value = 0

    if total_movement == 0:
        return returned_value

    average_mouvement = round(count_movement / total_movement)
    average_not_movement = round(count_not_movement / total_movement)

    if average_mouvement >= 0.8:
        returned_value = 1
    elif (average_mouvement <= 0.5 and average_not_movement <= 0.5):
        returned_value = 0.5
    elif (average_mouvement >= 0.3 and 0.3 >= average_not_movement <= 0.7):
        returned_value = 0.2
    elif (average_mouvement >= 0.4 and average_not_movement <= 0.6):
        returned_value = 0.4
    elif (average_mouvement >= 0.6 and average_not_movement <= 0.4):
        returned_value = 0.6

    return returned_value

def mouvement_user(data_mouvement: np) -> float | int:
    '''
        Model de kaggle https://www.kaggle.com/datasets/vmalyi/run-or-walk \n
        https://www.kaggle.com/code/abhishekgupta0695/walk-run-classification-accuracy-99
    '''
    with open('ModelPositionMovement/ModelRunOrWalk', 'rb') as file:
        model_mouvement_user = pickle.load(file)

    sequence_mouvements = []
    for data in data_mouvement:
        input_data = np.array([data])

        result = model_mouvement_user.predict(input_data)
        sequence_mouvements.append(result)

    total_mouvements = len(sequence_mouvements)
    count_movement = sum(prediction[0] == 1 for prediction in sequence_mouvements)
    count_not_movement = total_mouvements - count_movement

    return get_pourcentage_movement(count_movement, total_mouvements, count_not_movement)

def recommend_playlist(data_movement: np, data: DataFrame) -> DataFrame:
    user_movement: float | int = mouvement_user(data_movement)

    recommended_playlists: list = []
    if user_movement == 1:
        recommended_playlists =  data[data['type'] == 'sport']
    elif user_movement == 0:
        recommended_playlists = data[data['type'] == 'depressed']
    else: 
        if 0.2 <= user_movement <= 0.8:
            filtered_data = data[data['movement'].apply(lambda x: user_movement in x if isinstance(x, list) else False)]
            recommended_playlists = filtered_data[(filtered_data['energy'] >= user_movement) & (filtered_data['loudness'] <= user_movement)]

    recommended_playlists = recommended_playlists[['name', 'artist', 'type']]

    return recommended_playlists.sample(n=10)
