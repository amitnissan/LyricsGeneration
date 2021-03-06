import os
from config import *
from typing import Union, Tuple


class IllegalArgumentError(ValueError):
    pass


def get_user_input(from_interface: bool = False) -> Union[Tuple[str, str], Tuple[None, None]]:
    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print("\t\t♪♫♪ Welcome to our lyric generation machine ♪♫♪\n")
    artists = [f for f in os.listdir(lyrics_dir_path) if os.path.isfile(os.path.join(lyrics_dir_path, f))]
    artists_dict = {i: artist.replace('.csv', '') for i, artist in enumerate(artists)}

    if from_interface:
        artists = [f for f in os.listdir(output_dir) if '_trained' in f]
        artists_dict = {i: artist.replace('_trained', '') for i, artist in enumerate(artists)}

    if from_interface and not artists_dict:
        print("Unfortunately pretrained models failed to download.")
        print("You can rerun the script to try and download again, or train one yourself and use it!")
        return None, None

    print("Here are the artists for today:")

    for num_artist, artist in artists_dict.items():
        print(f"\t# {num_artist}: {artist.capitalize()}")

    while True:
        try:
            chosen_artist_number = int(input("\nPlease enter # of artist of choice: "))
            if chosen_artist_number not in artists_dict.keys():
                raise IllegalArgumentError
        except IllegalArgumentError:
            print(f"Please choose a number from the following list of artists:")
            for num_artist, artist in artists_dict.items():
                print(f"\t# {num_artist}: {artist}")
            continue
        except ValueError:
            print(f"Sorry, bad input. For example: type 0 for: {artists_dict[0]}")
            continue
        else:
            print(f"{artists_dict[chosen_artist_number]} is a great choice!")
            break

    chosen_prompt_text = input(
        f"\nEnter a sentence you wish {artists_dict[chosen_artist_number]} start with (for example: \"COVID-19 was like a\"...). Plain text no quotes needed: ")

    print("\n\n\n*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*")
    print(
        f"\t\t♪♫♪ Generating a new song by {artists_dict[chosen_artist_number].capitalize()} talking about \'{chosen_prompt_text}\'... ♪♫♪\n")

    return artists_dict[chosen_artist_number], chosen_prompt_text
