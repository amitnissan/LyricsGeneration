# Misc config
lyrics_dir_path = 'Data/'
text_for_fine_tune_file = 'text_for_fine_tune.txt'
output_dir = 'output'
device = 'cuda'

# fine tune hyperparameters
num_epoch = 3
batch_size = 2
seed = 42

# generating lyrics hyperparameters
temperature = 0.7
k = 20
p = 0.9
repetition_penalty = 1.0
num_return_sequences = 1  # num generated songs
length = 500
stop_token = '|EndOfText|'
