import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from data_preprocess import pull_lyrics
from user_input_console import get_user_input
from fine_tune import fine_tune
from interface import used_trained_models_to_generate_and_evaluate

def main():
    # get artist and prompt text from user
    chosen_artist, chosen_prompt_text = get_user_input()

    # pull lyrics
    pull_lyrics(chosen_artist)

    # fine tune DistilGPT2 with the lyrics
    fine_tune(chosen_artist)

    # generate lyrics and evaluate
    used_trained_models_to_generate_and_evaluate(chosen_artist, chosen_prompt_text)


if __name__ == '__main__':
    main()
