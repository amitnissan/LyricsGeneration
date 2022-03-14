from config import *
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def get_model_tokenizer(weights_dir):
    print("Loading Model ...")
    model = GPT2LMHeadModel.from_pretrained(weights_dir, local_files_only=True)
    # model.to(device) FIXME line doesnt work
    print("Model Loaded ...")
    tokenizer = GPT2Tokenizer.from_pretrained(weights_dir, local_files_only=True)
    return model, tokenizer


def generate_lyrics(prompt_text, model_dir=output_dir):
    model, tokenizer = get_model_tokenizer(model_dir)

    encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")

    # encoded_prompt = encoded_prompt.to(device) FIXME doesnt work

    output_sequences = model.generate(
        input_ids=encoded_prompt,
        max_length=length,
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
