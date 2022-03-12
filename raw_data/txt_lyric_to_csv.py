import pandas as pd

from config import lyrics_dir_path


def raw_txt_to_csv(artist: str):
    with open(f'{artist}_lyrics.txt', 'r') as f:
        output = f.read()
    song_df = pd.DataFrame([song for song in output.split('\n\n\n')])
    song_df = song_df.rename(columns={0: 'Lyrics'})
    song_df['Artist'] = artist.capitalize()
    song_df.to_csv(f'../{lyrics_dir_path}{artist.capitalize()}.csv', index=False)


if __name__ == '__main__':
    raw_txt_to_csv('avicii')
    raw_txt_to_csv('kanye')
    raw_txt_to_csv('beatles')
    raw_txt_to_csv('nirvana')
    raw_txt_to_csv('britneyspears')