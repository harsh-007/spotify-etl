# scripts/clean_and_transform.py
import pandas as pd
import os

def load_data(file_path):

    return pd.read_csv(file_path)

def clean_data(albums, tracks):

    unnecessary_columns = [
        'track_number', 'album_type',
        'album_id', 'artist_id', 'duration_sec'
    ]
    unnecessary_columns.extend([f'artist_{i}' for i in range(12)])
    albums = albums.drop(columns=unnecessary_columns)
    # Keep only relevant columns
    relevant_columns = ['track_name', 'track_id', 'label', 'release_date', 'total_tracks','duration_ms']
    albums['release_date'] = pd.to_datetime(albums['release_date'], errors='coerce')
    albums = albums.dropna(subset=relevant_columns)

    albums['radio_mix'] = albums['duration_ms'] <= 180000

    final_df = pd.merge(albums, tracks,
                        left_on='track_id',
                        right_on='id',
                        how='inner')

    final_df = final_df[(final_df['explicit'] == False) & (final_df['track_popularity'] > 50)]
    print(final_df.head())
    return final_df

def save_data(df, file_path):

    df.to_csv(file_path, index=False)


def main():

    # Load data
    albums = load_data('data/spotify-albums_data_2023.csv')
    tracks = load_data('data/spotify_tracks_data_2023.csv')
    cleaned_file_path = 'data/cleaned_data.csv'
    # Clean and transform data
    cleaned_df = clean_data(albums, tracks)
    save_data(cleaned_df, cleaned_file_path)


if __name__ == "__main__":
    main()