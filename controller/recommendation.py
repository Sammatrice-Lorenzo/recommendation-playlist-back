import flask
from model.recommendation_playlist import recommend_playlist
import numpy as np
import pandas as pd
import json


class Recommendation:
    def __init__(self, app: flask) -> None:
        self.app = app
        self.recommendation_blueprint = flask.Blueprint('model', __name__)
        self.init_route()
        self.app.register_blueprint(self.recommendation_blueprint)


    def init_route(self) -> None:
        self.recommendation_blueprint.route('/recommendation', methods=['POST'])(self.recommend_playlist_user)


    def recommend_playlist_user(self) -> json:

        data: pd.DataFrame = pd.read_csv('data/train_data.csv')
    
        try:
            movements_user: dict = flask.request.get_json()

            movement_to_numpy = []
            for movement in movements_user:
                movement_to_numpy.append(list(movement.values()))

            movement_to_numpy: np = np.array(movement_to_numpy)
            print(movement_to_numpy)

            playlist_user: pd.DataFrame = recommend_playlist(movement_to_numpy, data)

            playlist_returned: list = []
            playlist_user_updated: list = []

            for row_track_playlist in playlist_user.iterrows():
                track: dict[str, str] = {
                    'name': row_track_playlist[1]['name'],
                    'artist': row_track_playlist[1]['artist'] 
                }
                playlist_user_updated.append(track)

            playlist: dict[str, dict] = {
                'tracks': playlist_user_updated,
                'type': playlist_user['type'].iloc[0]
            }
            playlist_returned.append(playlist)

            return flask.jsonify(playlist_returned), 200
        except Exception as e:
            print("Error:", str(e))

            return flask.jsonify({'Une erreur est survenue': str(e)}), 500
