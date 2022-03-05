import subprocess
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from data_preprocess import pull_lyrics
from generate_lyrics import generate_messages
from user_input_console import get_user_input

# install transformers with 4.17.dev version
with open(f'install_dev_transformers.sh', 'rb') as file:
    script = file.read()
_ = subprocess.call(script, shell=True)

from config import *
from fine_tune import get_model_tokenizer, fine_tune


def main():
    # get artist and prompt text from user
    chosen_artist, chosen_prompt_text = get_user_input()

    # pull lyrics
    file_name, output_dir = pull_lyrics(chosen_artist)

    #fine tune DistilGPT2 with the lyrics
    fine_tune(file_name, output_dir)

    model, tokenizer = get_model_tokenizer(output_dir, device='cuda')

    generated_sequences = generate_messages(
        model,
        tokenizer,
        chosen_prompt_text,
        stop_token,
        length,
        num_return_sequences,
        temperature=temperature,
        k=k,
        p=p,
        repetition_penalty=repetition_penalty
    )

    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(f"\t\t♪♫♪ This is \'{chosen_prompt_text}\' by {chosen_artist} ♪♫♪\n")
    print(generated_sequences)

if __name__ == '__main__':
    main()
