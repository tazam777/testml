import json
import torch
from transformers import GPT2Tokenizer, GPTJForCausalLM, Trainer, TrainingArguments
from torch.utils.data import Dataset, DataLoader

# Load the JSON data
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Tokenize the data
def tokenize_data(data, tokenizer, max_length=512):
    inputs, outputs = [], []
    tokenizer.pad_token = tokenizer.eos_token  # Set the EOS token as the padding token
    for item in data:
        encoded_input = tokenizer.encode(item['input'], truncation=True, max_length=max_length, padding="max_length")
        encoded_output = tokenizer.encode(json.dumps(item['output']), truncation=True, max_length=max_length, padding="max_length")
        inputs.append(encoded_input)
        outputs.append(encoded_output)
    return inputs, outputs

# Custom dataset class
class APIDocumentationDataset(Dataset):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        item = {'input_ids': torch.tensor(self.inputs[idx], dtype=torch.long),
                'labels': torch.tensor(self.outputs[idx], dtype=torch.long)}
        return item

# Function to train the model
def train_model(data_path, model_name, output_dir='./model_output', epochs=3, batch_size=2):
    # Load and prepare data
    data = load_dataset(data_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    inputs, outputs = tokenize_data(data, tokenizer)
    dataset = APIDocumentationDataset(inputs, outputs)

    # Optional: Split dataset into training and evaluation sets if no separate eval dataset
    train_size = int(0.9 * len(dataset))
    eval_size = len(dataset) - train_size
    train_dataset, eval_dataset = torch.utils.data.random_split(dataset, [train_size, eval_size])

    # Load model
    model = GPTJForCausalLM.from_pretrained(model_name)
    
    # Define training arguments with evaluation
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        logging_dir='./logs',
        save_strategy="epoch",
        evaluation_strategy="epoch",  # Set evaluation strategy
        load_best_model_at_end=True,
        metric_for_best_model='loss'  # Assuming you want to minimize loss; adjust as necessary
    )
    
    # Initialize Trainer with evaluation dataset
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,  # Include eval dataset for evaluation
        tokenizer=tokenizer
    )
    
    # Start training
    trainer.train()

    # Save the trained model and tokenizer
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
# Correct the path to your dataset and specify the model name
data_path = '/Users/tariqueanwarmulla/Desktop/SwaggerProj/data.json'  # Update this path
model_name = 'EleutherAI/gpt-j-6B'

# Execute the training function
train_model(data_path, model_name)
