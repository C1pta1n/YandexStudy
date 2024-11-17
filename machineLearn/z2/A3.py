import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import requests
import json

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print('{} device is available'.format(device))

# Скачать текст
url = 'https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/onegin.txt'
file_path = "onegin.txt"
response = requests.get(url)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(response.text)

# Чтение и обработка текста
with open('onegin.txt', 'r', encoding='utf-8', errors='ignore') as iofile:
    text = iofile.readlines()

# Обработка текста
text = "".join([x.replace('\t\t', '').lower() for x in text])

# Создание токенов
tokens = sorted(set(text.lower())) + ['<sos>']
num_tokens = len(tokens)
assert num_tokens == 84, "Check the tokenization process"

# Создание словаря для токенов и их индексов
token_to_idx = {x: idx for idx, x in enumerate(tokens)}
idx_to_token = {idx: x for idx, x in enumerate(tokens)}

# Печать успешной загрузки
print("Seems fine!")

# Преобразование текста в индексы
text_encoded = [token_to_idx[x] for x in text]

# Настройки генерации
batch_size = 256
seq_length = 100
start_column = np.zeros((batch_size, 1), dtype=int) + token_to_idx['<sos>']

# Генерация данных для обучения
def generate_chunk():
    global text_encoded, start_column, batch_size, seq_length
    start_index = np.random.randint(0, len(text_encoded) - batch_size * seq_length - 1)
    data = np.array(text_encoded[start_index:start_index + batch_size * seq_length]).reshape((batch_size, -1))
    yield np.hstack((start_column, data))

# Преобразование индексов в one-hot вектор
def convert_to_one_hot(x_sequence, num_tokens):
    one_hot = F.one_hot(x_sequence, num_tokens)  # (batch_size, seq_len, num_tokens)
    return one_hot.float()  # Преобразуем в тип float, так как LSTM ожидает input_size float

# Генерация текста
# Генерация текста
def generate_sample(char_rnn, seed_phrase=None, max_length=500, temperature=1.0, device='cpu'):
    # Инициализируем исходную последовательность
    if seed_phrase is not None:
        x_sequence = [token_to_idx['<sos>']] + [token_to_idx[token] for token in seed_phrase]
    else:
        x_sequence = [token_to_idx['<sos>']]

    # Преобразуем последовательность в тензор
    x_sequence = torch.tensor([x_sequence], dtype=torch.int64).to(device)
    x_sequence_one_hot = convert_to_one_hot(x_sequence, num_tokens).to(device)
    
    generated_text = seed_phrase if seed_phrase else ""
    char_rnn.eval()

    print("Starting text generation...")
    
    # Модель генерирует текст до max_length символов
    while len(generated_text) < max_length:
        # Генерируем следующий символ
        output = char_rnn(x_sequence_one_hot)  # Результат работы модели
        last_output = output[0, -1, :]  # Последний выход
        last_output = last_output / temperature  # Регулируем температуру
        probs = F.softmax(last_output, dim=0).cpu().data.numpy()  # Получаем вероятности
        next_idx = np.random.choice(len(probs), p=probs)  # Выбираем следующий символ

        # Обновляем последовательность
        x_sequence = torch.cat((x_sequence, torch.tensor([[next_idx]], dtype=torch.int64).to(device)), dim=1)
        x_sequence_one_hot = convert_to_one_hot(x_sequence, num_tokens).to(device)  # Обновляем one-hot

        # Добавляем символ к сгенерированному тексту
        generated_text += tokens[next_idx]

        # Логируем количество сгенерированных символов
        if len(generated_text) % 100 == 0:
            print(f"Generated {len(generated_text)} characters...")

        # Проверяем, достигнут ли лимит
        if len(generated_text) >= max_length:
            print(f"Generated phrase length: {len(generated_text)}")
            break  # Завершаем цикл

    # Дополняем текст до 500 символов, если нужно
    additional_chars = max_length - len(generated_text)
    if additional_chars > 0:
        print(f"Adding {additional_chars} characters to meet the length.")
        generated_text += ' ' * additional_chars  # Дополняем пробелами

    # Ограничиваем длину текста до max_length
    generated_text = generated_text[:max_length]

    # Проверка, что длина соответствует ожидаемой
    print(f"Generated phrase length: {len(generated_text)}")
    if len(generated_text) != max_length:
        print(f"Warning: Generated text length is {len(generated_text)} instead of {max_length}.")
        # Заполняем оставшееся количество символов пробелами
        generated_text += ' ' * (max_length - len(generated_text))

    return generated_text



# Определение модели CharRNN
class CharRNN(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers):
        super(CharRNN, self).__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=hidden_size, num_layers=num_layers)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        out, _ = self.lstm(x)  # Выход LSTM
        out = self.fc(out)  # Линейный слой для преобразования
        return out  # Возвращаем только выход

# Инициализация модели
model = CharRNN(len(tokens), 256, 2).to(device)

# Генерация одной фразы
temperature = 0.8

generated_phrase = generate_sample(
    model,
    ' мой дядя самых честных правил',
    max_length=500,
    temperature=temperature,
    device=device
).replace('<sos>', '')

# Проверка и сохранение результата
if not isinstance(generated_phrase, str):
    raise ValueError("The generated phrase should be a string")
assert all([x in set(tokens) for x in set(list(generated_phrase))]), 'Unknown tokens detected, check your submission!'

# Сохранение результата в файл
submission_dict = {
    'token_to_idx': token_to_idx,
    'generated_phrases': [generated_phrase]
}

with open('submission_dict.json', 'w') as iofile:
    json.dump(submission_dict, iofile)

print('File saved to `submission_dict.json`')
