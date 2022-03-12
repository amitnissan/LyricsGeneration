import subprocess
from config import *


def fine_tune():
    cmd = '''
    python transformers/examples/pytorch/language-modeling/run_clm.py \
        --model_name_or_path distilgpt2 \
        --train_file {0} \
        --do_train \
        --num_train_epochs {2} \
        --overwrite_output_dir \
        --per_device_train_batch_size {3} \
        --output_dir {1}
        --seed {4}
    '''.format(text_for_fine_tune_file, output_dir, num_epoch, batch_size, seed)
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
