from creation_data import Dataset

def main():
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
    main()