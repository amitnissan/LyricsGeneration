import pandas as pd

if __name__ == '__main__':
    with open('avicii_lyrics.txt', 'r') as f:
        output = f.read()
    song_df = pd.DataFrame([song for song in output.split('\n\n\n')])
    song_df = song_df.rename(columns={0: 'Lyrics'})
    song_df['Artist'] = 'Avicii'
    song_df.to_csv('../Data/Avicii.csv', index=False)