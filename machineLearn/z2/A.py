import string
import os
from random import sample

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from IPython.display import clear_output

import matplotlib.pyplot as plt
import json
import requests

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print('{} device is available'.format(device))

url = 'https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/onegin.txt'
file_path = "onegin.txt"
response = requests.get(url)

with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

with open('onegin.txt', 'r', encoding='utf-8', errors = 'ignore') as iofile:
    text = iofile.readlines()
    
text = "".join([x.replace('\t\t', '').lower() for x in text])

tokens = sorted(set(text.lower())) + ['<sos>']
num_tokens = len(tokens)

assert num_tokens == 84, "Check the tokenization process"

token_to_idx = {x: idx for idx, x in enumerate(tokens)}
idx_to_token = {idx: x for idx, x in enumerate(tokens)}

assert len(tokens) == len(token_to_idx), "Mapping should be unique"

print("Seems fine!")


text_encoded = [token_to_idx[x] for x in text]

batch_size = 256
seq_length = 100
start_column = np.zeros((batch_size, 1), dtype=int) + token_to_idx['<sos>']

def generate_chunk():
    global text_encoded, start_column, batch_size, seq_length

    start_index = np.random.randint(0, len(text_encoded) - batch_size*seq_length - 1)
    data = np.array(text_encoded[start_index:start_index + batch_size*seq_length]).reshape((batch_size, -1))
    yield np.hstack((start_column, data))
    
def generate_sample(char_rnn, seed_phrase=None, max_length=200, temperature=1.0, device='cpu'):
    if seed_phrase is not None:
        x_sequence = [token_to_idx['<sos>']] + [token_to_idx[token] for token in seed_phrase]
    else: 
        x_sequence = [token_to_idx['<sos>']]
    x_sequence = torch.tensor([x_sequence], dtype=torch.int64).to(device)
    generated_text = seed_phrase if seed_phrase else ""
    char_rnn.eval()

    for _ in range(max_length - len(x_sequence[0])):
        output, _ = char_rnn(x_sequence)
        last_output = output[0, -1, :]
        last_output = last_output / temperature
        probs = F.softmax(last_output, dim=0).cpu().data.numpy()
        next_idx = np.random.choice(len(probs), p=probs)
        x_sequence = torch.cat((x_sequence, torch.tensor([[next_idx]], dtype=torch.int64).to(device)), dim=1)
        generated_text += tokens[next_idx]
        temperature = 0.8

    return generated_text

class CharRNN(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers):
        super(CharRNN, self).__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=hidden_size, num_layers=num_layers)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out

model = CharRNN(len(tokens), 256, 2).to(device)

temperature = 0.8

generated_phrases = [
    generate_sample(
    model,
    ' мой дядя самых честных правил', 
    max_length=500,                    
    temperature=temperature,          
    device=device                    
    ).replace('<sos>', '') 
    for _ in range(10)
    ]

if 'generated_phrases' not in locals():
    raise ValueError("Please, save generated phrases to `generated_phrases` variable")

for phrase in generated_phrases:
    if not isinstance(phrase, str):
        raise ValueError("The generated phrase should be a string")
    if len(phrase) != 500:
        raise ValueError("The `generated_phrase` length should be equal to 500")
    assert all([x in set(tokens) for x in set(list(phrase))]), 'Unknown tokens detected, check your submission!'

submission_dict = {
    'token_to_idx': token_to_idx,
    'generated_phrases': generated_phrases
}

with open('submission_dict.json', 'w') as iofile:
    json.dump(submission_dict, iofile)

print('File saved to `submission_dict.json`')