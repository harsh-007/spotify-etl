from kaggle.api.kaggle_api_extended import KaggleApi
import os
def download_dataset():
    api = KaggleApi()
    api.authenticate()
    if not os.path.exists('data/'):
        os.makedirs('data/')
    api.dataset_download_files("tonygordonjr/spotify-dataset-2023", path='data/', unzip=True)
if __name__ == "__main__":
    download_dataset()