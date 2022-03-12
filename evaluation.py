import pandas as pd
from bert_score import score, plot_example
from config import *

def evaluate(generated_sequences, chosen_artist):

    data = pd.read_csv(f'{lyrics_dir_path}{chosen_artist}.csv')
    texts = list(set(data.Lyrics))

    P, R, F1 = score(generated_sequences, texts[:num_return_sequences], lang="en", verbose=True)
    P = P.tolist()
    R = R.tolist()
    F1 = F1.tolist()
    best_lyrics_index = F1.index(max(F1))

    # Cosine similarity matrix between the generated text and some input text
    # plot_example(generated_sequences[0], texts[0], lang="en")

    return P, R, F1, best_lyrics_index