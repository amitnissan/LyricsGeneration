import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# install transformers with 4.17.dev version
with open(f'install_dev_transformers.sh', 'rb') as file:
    script = file.read()
_ = subprocess.call(script, shell=True)


from evaluation import evaluate
from generate_lyrics import generate_lyrics
from user_input_console import get_user_input


def recreate_results():
    # get artist and prompt text from user
    chosen_artist, chosen_prompt_text = get_user_input()

    # use fine tuned model for lyrics generation tasks given a subject
    generated_sequences = generate_lyrics(chosen_prompt_text, 'chosen_models/'+chosen_artist.lower())

    # evaluate generated lyrics
    P, R, F1, best_lyrics_index = evaluate(generated_sequences, chosen_artist)

    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(f"\t\t♪♫♪ This is \'{chosen_prompt_text}\' by {chosen_artist} ♪♫♪\n")
    print(generated_sequences[best_lyrics_index])

    print(f"Precision: {P[best_lyrics_index]}")
    print(f"Recall: {R[best_lyrics_index]}")
    print(f"F1: {F1[best_lyrics_index]}")


if __name__ == '__main__':
    recreate_results()
