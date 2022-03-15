# Misc config
lyrics_dir_path = 'Data/'
text_for_fine_tune_file = 'text_for_fine_tune.txt'
output_dir = 'trained_models'
device = 'cuda'

# fine tune hyperparameters
num_epoch = 20
batch_size = 2
seed = 42

# generating lyrics hyperparameters
temperature = 0.7
k = 40
p = 0.9
repetition_penalty = 3.0
num_return_sequences = 20  # num generated songs
length = 300
stop_token = '|EndOfText|'


trained_files_drive_id = {
    'avicii_trained':           '1ghZclFond80_I-D9OZphk_xm7SpBbfso',
    'beatles_trained':          '1YT9TYVbtGkNZ4I41RNvzHGvJhBYciHGi',
    'britneyspears_trained':    '1omMEmvNO31seBIGqhxkOGr0vBPKDawbL',
    'kanye_trained':            '1jx8q7US8N0g8voX5gD3AvBca2eqPPdz0',
    'nirvana_trained':          '1LDVwdp9mznxBUFO2438B3P_oc-XMEnLa'
}

