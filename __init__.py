from builder.creation_data import Dataset
from controller.recommendation import Recommendation
import flask
import os
from flask_cors import CORS
from flask_sslify import SSLify
from dotenv import load_dotenv


app: flask = flask.Flask(__name__)
load_dotenv()


def build_data_set() -> None:
    """Si vous devez créer la dataset appeler la function dans __main__
    """
    dataset = Dataset()

    playlists = [
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1E35x0QGP9VzOh',
            'type': 'walk',
            'movement': [0.5, 0.6, 0.7],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1EIesbtlhD4Mon',
            'type': 'sport',
            'movement': [0.8, 0.9, 1],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1EIggeYqvv7G8A',
            'type': 'chill',
            'movement': [0.2, 0.3 , 0.4],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1EIcVZUMP507A4',
            'type': 'sport',
            'movement': [0.8, 0.9, 1],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1EVKuMoAJjoTIw',
            'type': 'depressed',
            'movement': [0],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1EIcZUgkA3BSiL',
            'type': 'depressed',
            'movement': [0],
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp',
            'type': 'sleep',
            'movement': [0, 0.2]
        },
    ]

    dataset.create_data_set(playlists)

if __name__ == "__main__":

    CORS(app, resources={r"/recommendation": {"origins": os.getenv('URL_FRONT')}})

    Recommendation(app=app)
    context = ('config/ssl/cert.pem', 'config/ssl/key.pem')
    sslify = SSLify(app, permanent=True)

    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)
    # http_server = WSGIServer(('0.0.0.0', 5000), app, keyfile='config/ssl/key.pem', certfile='config/ssl/cert.pem')
    # http_server.serve_forever()

