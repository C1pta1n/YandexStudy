import numpy as np
from typing import Tuple

def softmax(vector: np.ndarray) -> np.ndarray:
    if vector.ndim == 1:
        vector = vector - np.max(vector)
        exp_vector = np.exp(vector)
        return exp_vector / np.sum(exp_vector)
    elif vector.ndim == 2:
        vector = vector - np.max(vector, axis=1, keepdims=True) 
        exp_vector = np.exp(vector)
        return exp_vector / np.sum(exp_vector, axis=1, keepdims=True)
    else:
        raise ValueError(f"Expected 1D or 2D vector, but got {vector.ndim}D.")

def multiplicative_attention(
    decoder_hidden_state: np.ndarray, 
    encoder_hidden_states: np.ndarray, 
    W_mult: np.ndarray
) -> np.ndarray:
    if decoder_hidden_state.shape != (5, 1):
        raise ValueError(f"Expected decoder_hidden_state to have shape (5, 1), but got {decoder_hidden_state.shape}")
    if W_mult.shape != (3, 5):
        raise ValueError(f"Expected W_mult to have shape (3, 5), but got {W_mult.shape}")
    transformed_decoder_state = W_mult @ decoder_hidden_state  
    attention_scores = encoder_hidden_states.T @ transformed_decoder_state  
    attention_weights = softmax(attention_scores.T) 
    attention_vector = encoder_hidden_states @ attention_weights.T 
    
    return attention_vector

def additive_attention(
    decoder_hidden_state: np.ndarray, 
    encoder_hidden_states: np.ndarray, 
    v_add: np.ndarray, 
    W_add_enc: np.ndarray, 
    W_add_dec: np.ndarray
) -> np.ndarray:
    if W_add_enc.shape[1] != encoder_hidden_states.shape[0]:
        raise ValueError("Mismatch between W_add_enc and encoder_hidden_states dimensions.")
    if W_add_dec.shape[1] != decoder_hidden_state.shape[0]:
        raise ValueError("Mismatch between W_add_dec and decoder_hidden_state dimensions.")
    if v_add.shape[0] != W_add_enc.shape[0]:
        raise ValueError("Mismatch between v_add and W_add_enc dimensions.")
    encoder_combined = W_add_enc @ encoder_hidden_states 
    decoder_combined = W_add_dec @ decoder_hidden_state  
    combined_state = encoder_combined + decoder_combined  

    activation = np.tanh(combined_state)

    attention_scores = v_add.T @ activation  
    exp_attention_scores = np.exp(attention_scores) 
    attention_weights = exp_attention_scores / np.sum(exp_attention_scores, axis=1, keepdims=True)
    attention_vector = encoder_hidden_states @ attention_weights.T 
    
    return attention_vector
