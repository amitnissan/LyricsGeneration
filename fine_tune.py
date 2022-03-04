import subprocess
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def fine_tune(file_name, output_dir):
    cmd = '''
    python transformers/examples/pytorch/language-modeling/run_clm.py \
        --model_name_or_path distilgpt2 \
        --train_file {0} \
        --do_train \
        --num_train_epochs 3 \
        --overwrite_output_dir \
        --per_device_train_batch_size 2 \
        --output_dir {1}
    '''.format(file_name, output_dir)
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def get_model_tokenizer(weights_dir, device='cuda'):
    print("Loading Model ...")
    model = GPT2LMHeadModel.from_pretrained(weights_dir)
    # model.to('cuda') FIXME line doesnt work
    print("Model Loaded ...")
    tokenizer = GPT2Tokenizer.from_pretrained(weights_dir)
    return model, tokenizer
