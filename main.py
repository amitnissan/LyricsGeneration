import subprocess
import os
import pandas as pd

import config
from config import *


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# install transformers with 4.17.dev version
with open(f'install_dev_transformers.sh', 'rb') as file:
    script = file.read()
_ = subprocess.call(script, shell=True)

from data_preprocess import pull_lyrics
from generate_lyrics import generate_lyrics
from user_input_console import get_user_input
from fine_tune import fine_tune
from bert_score import score, plot_example

def main():
    # get artist and prompt text from user
    chosen_artist, chosen_prompt_text = get_user_input()

    # pull lyrics
    pull_lyrics(chosen_artist)

    # fine tune DistilGPT2 with the lyrics
    fine_tune()

    generated_sequences = generate_lyrics(chosen_prompt_text)

    data = pd.read_csv(f'{lyrics_dir_path}{chosen_artist}.csv')
    texts = list(set(data.Lyrics))

    print(f"input {len(texts[:config.num_return_sequences])}")
    print(f"output {len(generated_sequences)}")

    print("Evaluating generated lyrics...")
    P, R, F1 = score(generated_sequences, texts[:config.num_return_sequences], lang="en", verbose=True)
    P = P.tolist()
    R = R.tolist()
    F1 = F1.tolist()

    # Cosine similarity matrix between the generated text and some input text
    # plot_example(generated_sequences[0], texts[0], lang="en")

    best_lyrics_index = F1.index(max(F1))
    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(f"\t\t♪♫♪ This is \'{chosen_prompt_text}\' by {chosen_artist} ♪♫♪\n")
    print(generated_sequences[best_lyrics_index])

    print(f"Precision: {P[best_lyrics_index]}")
    print(f"Recall: {R[best_lyrics_index]}")
    print(f"F1: {F1[best_lyrics_index]}")


if __name__ == '__main__':
    main()
