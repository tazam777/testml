import torch
from transformers import GPT2Tokenizer, GPTJForCausalLM
import json
import os

def load_or_download_model(model_name, model_dir, tokenizer_dir):
    """ Load or download the model and tokenizer """
    if not os.path.exists(model_dir) or not os.path.exists(tokenizer_dir):
        print("Downloading and saving the model and tokenizer...")
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPTJForCausalLM.from_pretrained(model_name)
        model.save_pretrained(model_dir)
        tokenizer.save_pretrained(tokenizer_dir)
    else:
        print("Loading the model and tokenizer from local directory...")
        model = GPTJForCausalLM.from_pretrained(model_dir)
        tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_dir)
    return model, tokenizer

def prepare_input(input_text, tokenizer, max_length=512):
    """ Tokenize and prepare the input for the model """
    encoded_input = tokenizer.encode(input_text, return_tensors='pt', truncation=True, max_length=max_length, padding="max_length")
    return encoded_input

def generate_output(model, tokenizer, input_tensor):
    """ Generate model output using the provided input tensor """
    model.eval()
    with torch.no_grad():
        output = model.generate(input_tensor, max_length=512)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded_output

def main():
    model_name = "EleutherAI/gpt-j-6B"
    model_dir = './gpt-j-6B_model'
    tokenizer_dir = './gpt-j-6B_tokenizer'
    model, tokenizer = load_or_download_model(model_name, model_dir, tokenizer_dir)

    print("Enter your Python code snippet:")
    input_text = input()  # Take input from the user via terminal

    input_tensor = prepare_input(input_text, tokenizer)
    generated_text = generate_output(model, tokenizer, input_tensor)

    # Assuming the output is JSON formatted text, parse it to format the output nicely
    try:
        formatted_output = json.dumps(json.loads(generated_text), indent=2)
        print("Generated Swagger Documentation:")
        print(formatted_output)
    except json.JSONDecodeError:
        print("Failed to parse the model output as JSON. Here's the raw output:")
        print(generated_text)

if __name__ == "__main__":
    main()
