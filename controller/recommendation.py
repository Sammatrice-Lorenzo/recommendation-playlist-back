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

        movements_user: dict = flask.request.get_json()
        print(movements_user)

        movements_user: np = np.array(list(movements_user))


        playlist_user: pd.DataFrame = recommend_playlist(movements_user, data)

        return flask.jsonify(playlist_user.to_json()), 200
