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
