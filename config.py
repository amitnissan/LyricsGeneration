# Misc config
lyrics_dir_path = 'Data/'
text_for_fine_tune_file = 'text_for_fine_tune.txt'
output_dir = 'output'
device = 'cuda'

# fine tune hyperparameters
num_epoch = 40
batch_size = 2
seed = 42

# generating lyrics hyperparameters
temperature = 0.4
k = 20
p = 0.9
repetition_penalty = 3.0
num_return_sequences = 20  # num generated songs
length = 600
stop_token = '|EndOfText|'
