import pandas as pd
from config import *


def pull_lyrics(chosen_artist: str, keep_newlines = True):
    data = pd.read_csv(f'{lyrics_dir_path}{chosen_artist}.csv')
    texts = list(set(data.Lyrics))
    if not keep_newlines:
        texts = [t.replace('\n',' ') for t in texts] #TODO check if this is better
    with open(text_for_fine_tune_file, 'w') as f:
        f.write(f" {stop_token}\n".join(texts))
