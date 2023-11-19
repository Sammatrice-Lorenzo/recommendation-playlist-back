# https://open.spotify.com/playlist/37i9dQZF1E35x0QGP9VzOh => Rap Ita
# https://open.spotify.com/playlist/4KHJvDrRTzeI0dKJN1CYbc    => Tech

# https://open.spotify.com/playlist/5Cxad6lnpi2e1RI6MNZ3MU => rap ita

# https://open.spotify.com/playlist/37i9dQZF1DX1X23oiQRTB5 fr

# https://open.spotify.com/playlist/2kiAjbrOmBt770igmhQYsM?si=X4w0HaDhRnSP2HTnd7oJNg -> random 


from creation_data import Dataset
import numpy
import pandas as pd

def main():
    dataset = Dataset()
    # tracks = pd.read_csv('./data/train_data.csv')
    # # tracks = tracks.iloc[147:200]
    # # tracks = tracks.iloc[50:104]
    # # tracks = tracks.iloc[0:49]
    # # tracks = tracks.iloc[201:250]
    # tracks = tracks.iloc[251:280]

    # df_data = []
    # for index, row in tracks.iterrows():
    #     print(row['energy'])
    #     mouvement = dataset.threshold_mouvement(row['energy'], row['valence'], row['tempo'], row['loudness'])
    #     df_data.append({
    #     'artist': row['artist'],
    #     'name': row['name'],
    #     'mouvement': mouvement,
    #     'energy': row['energy'],
    #     'valence': row['valence'],
    #     'loudness': row['loudness'],
    #     'tempo': row['tempo']
    # })

    # df = pd.DataFrame(df_data)

    # print(df)


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

    # Rap it
    playlist_url = "https://open.spotify.com/playlist/37i9dQZF1E35x0QGP9VzOh"
    # Tech 
    # playlist_url = "https://open.spotify.com/playlist/4KHJvDrRTzeI0dKJN1CYbc"
    
    # random
    # playlist_url = "https://open.spotify.com/playlist/2kiAjbrOmBt770igmhQYsM?si=X4w0HaDhRnSP2HTnd7oJNg"
    
    # triste
    # playlist_url = "https://open.spotify.com/playlist/7CbFoucdKwMXDrKpFt0bE1"
    # playlist_url = "https://open.spotify.com/playlist/5qi7dUfd3QlY8OlzFsOcy0"
    dataset.create_data_set(playlists)



if __name__ == "__main__":
    main()