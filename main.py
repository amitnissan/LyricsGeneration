import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# install transformers with 4.17.dev version
with open(f'install_dev_transformers.sh', 'rb') as file:
    script = file.read()
_ = subprocess.call(script, shell=True)

from data_preprocess import pull_lyrics
from generate_lyrics import generate_lyrics
from user_input_console import get_user_input
from fine_tune import fine_tune


def main():
    # get artist and prompt text from user
    chosen_artist, chosen_prompt_text = get_user_input()

    # pull lyrics
    pull_lyrics(chosen_artist)

    # fine tune DistilGPT2 with the lyrics
    fine_tune()

    generated_sequences = generate_lyrics(chosen_prompt_text)

    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(f"\t\t♪♫♪ This is \'{chosen_prompt_text}\' by {chosen_artist} ♪♫♪\n")
    print(generated_sequences)


if __name__ == '__main__':
    main()
