import pandas as pd
import subprocess
from transformers import GPT2LMHeadModel, GPT2Tokenizer

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


def get_model_tokenizer(weights_dir, device='cuda'):
    print("Loading Model ...")
    model = GPT2LMHeadModel.from_pretrained(weights_dir)
    # model.to('cuda') FIXME line doesnt work
    print("Model Loaded ...")
    tokenizer = GPT2Tokenizer.from_pretrained(weights_dir)
    return model, tokenizer


def generate_messages(
        model,
        tokenizer,
        prompt_text,
        stop_token,
        length,
        num_return_sequences,
        temperature=0.7,
        k=20,
        p=0.9,
        repetition_penalty=1.0,
        device='cuda'
):
    MAX_LENGTH = int(10000)

    def adjust_length_to_model(length, max_sequence_length):
        if length < 0 and max_sequence_length > 0:
            length = max_sequence_length
        elif 0 < max_sequence_length < length:
            length = max_sequence_length  # No generation bigger than model size
        elif length < 0:
            length = MAX_LENGTH  # avoid infinite loop
        return length

    length = adjust_length_to_model(length=length, max_sequence_length=model.config.max_position_embeddings)

    encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")

    # encoded_prompt = encoded_prompt.to(device) FIXME doesnt work

    output_sequences = model.generate(
        input_ids=encoded_prompt,
        max_length=length + len(encoded_prompt[0]),
        temperature=temperature,
        top_k=k,
        top_p=p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        num_return_sequences=num_return_sequences,
    )

    if len(output_sequences.shape) > 2:
        output_sequences.squeeze_()

    generated_sequences = []

    for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
        # print("=== GENERATED SEQUENCE {} ===".format(generated_sequence_idx + 1))
        generated_sequence = generated_sequence.tolist()

        # Decode text
        text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)

        # Remove all text after the stop token
        text = text[: text.find(stop_token) if stop_token else None]

        # Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing
        total_sequence = (
                prompt_text + text[len(tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True)):]
        )

        generated_sequences.append(total_sequence)
    return generated_sequences

def main():
    # install transformers with 4.17.dev version
    with open('install_dev_transformers.sh', 'rb') as file:
        script = file.read()
    _ = subprocess.call(script, shell=True)

    # pull lyrics
    file_name, output_dir = pull_lyrics()

    #fine tune DistilGPT2 with the lyrics
    fine_tune(file_name, output_dir)

    model, tokenizer = get_model_tokenizer(output_dir, device='cuda')
    temperature = 1.0
    k = 400
    p = 0.9
    repetition_penalty = 1.0
    num_return_sequences = 5
    length = 1000
    stop_token = '|EndOfText|'
    prompt_text = "this is"

    generated_sequences = generate_messages(
        model,
        tokenizer,
        prompt_text,
        stop_token,
        length,
        num_return_sequences,
        temperature=temperature,
        k=k,
        p=p,
        repetition_penalty=repetition_penalty
    )

    print(generated_sequences)

if __name__ == '__main__':
    main()
