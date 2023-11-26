import pandas as pd
import numpy as np
from pandas import DataFrame
import pickle
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=FutureWarning)


data = pd.read_csv('./data/train_data.csv')

def mouvement_user(data_mouvement: np) -> float:
    with open('./ModelPositionMovement/ModelRunOrWalk', 'rb') as file:
        model_mouvement_user = pickle.load(file)

    sequence_mouvements = []
    for data in data_mouvement:
        input_data = np.array([data])

        result = model_mouvement_user.predict(input_data)
        sequence_mouvements.append(result)

    total_mouvements = len(sequence_mouvements)
    count_mouvement = sum(prediction[0] == 1 for prediction in sequence_mouvements)
    count_not_mouvement = total_mouvements - count_mouvement

    returned_value = 0

    average_mouvement = round(count_mouvement / total_mouvements)
    average_not_mouvement = round(count_not_mouvement / total_mouvements)

    if count_mouvement / total_mouvements >= 0.8:
        returned_value = 1
    elif (average_mouvement <= 0.5 and average_not_mouvement <= 0.5):
        returned_value = 0.5
    elif (average_mouvement >= 0.3 and 0.3 >= average_not_mouvement <= 0.7):
        returned_value = 0.2
    elif (average_mouvement >= 0.4 and average_not_mouvement <= 0.6):
        returned_value = 0.4
    elif (average_mouvement >= 0.6 and average_not_mouvement <= 0.4):
        returned_value = 0.6

    print(count_mouvement / total_mouvements)
    print(count_not_mouvement / total_mouvements)

    return returned_value

def recommend_playlist(data_movement: np, data: DataFrame):
    user_movement = mouvement_user(data_movement)
    print(user_movement)

    recommended_playlists = []
    if user_movement == 1:
        recommended_playlists =  data[data['type'] == 'sport']
    elif user_movement == 0:
        recommended_playlists = data[data['type'] == 'depressed']
    else: 
        if 0.2 <= user_movement <= 0.6:
            data['movement'] = data['movement'].apply(lambda x: eval(x) if isinstance(x, str) else x)
            filtered_data = data[data['movement'].apply(lambda x: user_movement in x if isinstance(x, list) else False)]
            recommended_playlists = filtered_data[(filtered_data['energy'] >= user_movement) & (filtered_data['loudness'] <= user_movement)]
    
    return recommended_playlists.sample(n=10)


# data_run = pd.read_csv('./dataset.csv').iloc[1:756, 5:11]
data_run = pd.read_csv('./data/dataset_movement.csv').iloc[756:1556, 5:11]
data_run = data_run.to_numpy()

print(recommend_playlist(data_movement=data_run, data=data))

