import pandas as pd
from sklearn.neighbors import NearestNeighbors

def recommend_playlist(user_movement, user_liked_features, weights, data):
    filtered_data = data[data['movement'] == user_movement]

    recommendation_features = filtered_data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

    weighted_features = recommendation_features.copy()
    for feature in weights:
        weighted_features[feature] *= weights[feature]

    knn_model = NearestNeighbors(n_neighbors=5)
    knn_model.fit(weighted_features)

    user_liked_df = pd.DataFrame([user_liked_features], columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])

    distances, indices = knn_model.kneighbors(user_liked_df, n_neighbors=5)
    recommended_indices = indices.flatten()

    return data.iloc[recommended_indices][['name', 'artist', 'genres', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'movement', 'liked']]

user_movement = 0.5
data = pd.read_csv('./data/train_data.csv')

# user_liked_features = {
#     'danceability': 0.671,
#     'energy': 0.876,
#     'key': 7,
#     'loudness': -5.681,
#     'mode': 0,
#     'speechiness': 0.0352,
#     'acousticness': 0.12,
#     'instrumentalness': 0.188,
#     'liveness': 0.0823,
#     'valence': 0.964,
#     'tempo': 129.998,
# }

user_liked_features = {
    'danceability': 0.555,
    'energy': 0.613,
    'key': 4,
    'loudness': -6.746,
    'mode': 0,
    'speechiness': 0.0368,
    'acousticness': 0.0619,
    'instrumentalness': 0.0,
    'liveness': 0.198,
    'valence': 0.0988,
    'tempo': 120.922,
}

weights = {
    'danceability': 1.5,
    'energy': 1.0,
    'loudness': 1.5,
}
# weights = {
#     'danceability': 1.5,
#     'energy': 10.0,
#     'loudness': 2.5,
# }

recommended_tracks = recommend_playlist(user_movement, user_liked_features, weights, data)
print(recommended_tracks)
