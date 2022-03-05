import pandas as pd
from config import *


def pull_lyrics(chosen_artist: str):
    data = pd.read_csv(f'{lyrics_dir_path}{chosen_artist}.csv')
    texts = list(set(data.Lyrics))
    with open(text_for_fine_tune_file, 'w') as f:
        f.write(f" {stop_token}\n".join(texts))
