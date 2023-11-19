from services.spotify_service import SpotifyService
import pandas as pd
from pandas import DataFrame

class Dataset():
    def __init__(self) -> None:
        self.spotify = SpotifyService().get_spotify()

    threshold_at_rest: float = 0.2 #repos
    threshold_moving: float = 0.5
    threshold_moving_fast: float = 0.8

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
    

    def threshold_movement(self, valence: float, energy: float, tempo: float, loudness: float) -> float:
        threshold_energy_limited: float = 0.2
        threshold_energy_moderate: float = 0.5
        threshold_energy_rapide: float = 0.8

        threshold_valence_limited: float = 0.3
        threshold_valence_moderate: float = 0.6
        threshold_valence_rapide: float = 0.9

        threshold_tempo_moderate: float = 120
        threshold_tempo_rapide: float = 140

        threshold_loudness_moderate: float = -10
        threshold_loudness_rapide: float = -5

        if energy < threshold_energy_limited and valence < threshold_valence_limited:
            return self.threshold_at_rest
        elif threshold_energy_limited <= energy <= threshold_energy_moderate and threshold_valence_limited <= valence <= threshold_valence_moderate:
            if tempo > threshold_tempo_rapide or loudness > threshold_loudness_rapide:
                return self.threshold_moving_fast
            elif tempo > threshold_tempo_moderate or loudness > threshold_loudness_moderate:
                return self.threshold_moving
            else:
                return self.threshold_at_rest
        elif energy > threshold_energy_rapide or valence > threshold_valence_rapide:
            return self.threshold_moving_fast
        else:
            return self.threshold_moving


    def build_movement_column_by_track(self, url_playlist: str) -> DataFrame:
        df_playlist = self.convert_playlist_to_data_frame(url_playlist)

        column_movement: list = []
        for index, row in df_playlist.iterrows():
            movement = self.threshold_movement(
                row['energy'], row['valence'], row['tempo'], row['loudness']
            )
            column_movement.append(movement)

        df_playlist['movement'] = column_movement

        return df_playlist
    
    def create_data_set(self, playlists: list) -> None:
        dataframes_playlists: list = []
        for playlist in playlists:
            df: DataFrame = self.build_movement_column_by_track(playlist['playlist'])
            df['liked'] = playlist['liked']
            dataframes_playlists.append(df)

        final_dataframe = pd.concat(dataframes_playlists, ignore_index=True)

        final_dataframe.to_csv('data/train_data.csv', index=False)

