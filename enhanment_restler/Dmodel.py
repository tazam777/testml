from transformers import GPTJForCausalLM, GPT2Tokenizer

# Specify the model you want to use
model_name = "EleutherAI/gpt-j-6B"

# This will download and cache the model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTJForCausalLM.from_pretrained(model_name)

# Save both the model and tokenizer to a directory of your choice
model.save_pretrained('./gpt-j-6B_model')
tokenizer.save_pretrained('./gpt-j-6B_tokenizer')