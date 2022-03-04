import pandas as pd
from config import *

def pull_lyrics():
    data = pd.read_csv('Data/Avicii.csv')
    texts = list(set(data.Lyrics))
    file_name = 'text_for_fine_tune.txt'
    output_dir = 'output'
    with open(file_name, 'w') as f:
        f.write(f" {stop_token}\n".join(texts))
    return file_name, output_dir