from creation_data import Dataset

def main():
    dataset = Dataset()

    playlists = [
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1E35x0QGP9VzOh',
            'liked': 1
        },
        {
            'playlist': 'https://open.spotify.com/playlist/4KHJvDrRTzeI0dKJN1CYbc',
            'liked': 1
        },
        {
            'playlist': 'https://open.spotify.com/playlist/5Cxad6lnpi2e1RI6MNZ3MU',
            'liked': 1
        },
        {
            'playlist': 'https://open.spotify.com/playlist/2kiAjbrOmBt770igmhQYsM?si=X4w0HaDhRnSP2HTnd7oJNg',
            'liked': 0
        },
        {
            'playlist': 'https://open.spotify.com/playlist/7CbFoucdKwMXDrKpFt0bE1',
            'liked': 0
        },
        {
            'playlist': 'https://open.spotify.com/playlist/37i9dQZF1DX1X23oiQRTB5',
            'liked': 1
        }
    ]

    dataset.create_data_set(playlists)

if __name__ == "__main__":
    main()