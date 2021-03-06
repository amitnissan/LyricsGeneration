import gdown
import os
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from evaluation import evaluate
from generate_lyrics import generate_lyrics
from user_input_console import get_user_input
from config import output_dir, trained_files_drive_id


def download_trained_models():
    for model,id in trained_files_drive_id.items():
        if not os.path.isdir(f'{output_dir}/{model}'):
            print(f"Downloading {model}")
            filenames = gdown.download_folder(id=id, output=output_dir+'/', use_cookies=False)
            if not filenames:
                print("Download failed, removing downloaded parts")
                shutil.rmtree(f'{output_dir}/{model}', ignore_errors=True)
        else:
            print(f"Model {model} exists")


def used_trained_models_to_generate_and_evaluate(chosen_artist, chosen_prompt_text, from_interface=False):
    # use fine tuned model for lyrics generation tasks given a subject
    dir = f'{output_dir}/{chosen_artist.lower()}' + ('_trained' if from_interface else '')
    generated_sequences = generate_lyrics(chosen_prompt_text, dir)

    # evaluate generated lyrics
    P, R, F1, best_lyrics_index = evaluate(generated_sequences, chosen_artist.capitalize())

    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(f"\t\t♪♫♪ This is \'{chosen_prompt_text}\' by {chosen_artist.capitalize()} ♪♫♪\n")
    print(generated_sequences[best_lyrics_index])

    print(f"Precision: {P[best_lyrics_index]}")
    print(f"Recall: {R[best_lyrics_index]}")
    print(f"F1: {F1[best_lyrics_index]}")


def main():
    # get artist and prompt text from user
    download_trained_models()
    chosen_artist, chosen_prompt_text = get_user_input(from_interface=True)
    if chosen_artist:
        used_trained_models_to_generate_and_evaluate(chosen_artist, chosen_prompt_text, from_interface=True)


if __name__ == '__main__':
    main()
