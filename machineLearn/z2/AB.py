import numpy as np

def multiplicative_attention(decoder_hidden_state, encoder_hidden_states, W_mult):
    transformed_encoder_states = np.dot(W_mult, encoder_hidden_states)
    attention_vector = np.dot(transformed_encoder_states.T, decoder_hidden_state)

    return attention_vector
def additive_attention(
    decoder_hidden_state, encoder_hidden_states, v_add, W_add_enc, W_add_dec):
    dec_att = W_add_dec @ decoder_hidden_state  
    enc_att = W_add_enc @ encoder_hidden_states 
    scores = enc_att + dec_att 
    scores = np.tanh(scores) 
    attention_weights = np.exp(scores)
    attention_weights /= np.sum(attention_weights, axis=1, keepdims=True)
    final_attention = attention_weights @ encoder_hidden_states.T 

    return final_attention.T

# Пример использования:
# decoder_hidden_state = np.random.rand(7, 1)  # Замените на фактическое состояние декодера
# encoder_hidden_states = np.random.rand(7, 10)  # Замените 10 на фактическое количество состояний

# final_vector = additive_attention(decoder_hidden_state, encoder_hidden_states, v_add, W_add_enc, W_add_dec)
# print(final_vector)