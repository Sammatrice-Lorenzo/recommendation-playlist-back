from services.spotify_service import SpotifyService
import pandas as pd
from pandas import DataFrame

class Dataset():
    def __init__(self) -> None:
        self.spotify = SpotifyService().get_spotify()

    def _get_tracks(self, playlist) -> list:
        return playlist['tracks']['items']

    def get_artist_genres(self, track):
        artist_id = track["track"]["artists"][0]['id']
        artist = self.spotify.artist(artist_id)

        return artist['genres']

    def create_data_frame_tracks(self, tracks: list) -> DataFrame:
        tracks_names = [track['track']['name'] for track in tracks]
        tracks_artists = [track['track']['artists'][0]['name'] for track in tracks]
        genres_names = [self.get_artist_genres(track) for track in tracks]
    
        return pd.DataFrame({'name': tracks_names, 'artist': tracks_artists, 'genres': genres_names})


    def create_data_frame_tracks_features(self, tracks_ids: list) -> DataFrame:
        tracks_features = [self.spotify.audio_features(track_id)[0] for track_id in tracks_ids]

        tracks_features_names = list(tracks_features[0].keys())
        tracks_features_values = [list(track_feature.values()) for track_feature in tracks_features]

        return pd.DataFrame(tracks_features_values, columns=tracks_features_names)

 
    def convert_playlist_to_data_frame(self, url_playlist: str) -> DataFrame:
        playlist = self.spotify.playlist(url_playlist)

        tracks: list = self._get_tracks(playlist=playlist)
        tracks_ids = [track['track']['id'] for track in tracks]

        df_tracks = self.create_data_frame_tracks(tracks)
        df_features = self.create_data_frame_tracks_features(tracks_ids)

        columns_to_exclude = ['id', 'uri', 'track_href', 'analysis_url', 'type']

        return pd.concat([df_tracks, df_features.drop(columns=columns_to_exclude)], axis=1)
    
    def create_data_set(self, playlists: list) -> None:
        dataframes_playlists: list = []
        for playlist in playlists:
            df: DataFrame = self.convert_playlist_to_data_frame(playlist['playlist'])
            df['type'] = playlist['type']
            df['movement'] = [playlist['movement']] * len(df)
            dataframes_playlists.append(df)

        final_dataframe = pd.concat(dataframes_playlists, ignore_index=True)

        final_dataframe.to_csv('data/train_data.csv', index=False)

