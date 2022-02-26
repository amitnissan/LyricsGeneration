import pandas as pd
import subprocess

def pull_lyrics():
    data = pd.read_csv('Data/Avicii.csv')
    texts = list(set(data.Lyrics))
    file_name = 'text_for_fine_tune.txt'
    output_dir = 'output'
    with open(file_name, 'w') as f:
        f.write(" |EndOfText|\n".join(texts))
    return file_name, output_dir

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

def main():
    # install transformers with 4.17.dev version
    with open('install_dev_transformers.sh', 'rb') as file:
        script = file.read()
    _ = subprocess.call(script, shell=True)

    # pull lyrics
    file_name, output_dir = pull_lyrics()

    #fine tune DistilGPT2 with the lyrics
    fine_tune(file_name, output_dir)

if __name__ == '__main__':
    main()
