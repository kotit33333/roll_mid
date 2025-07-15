from sklearn.linear_model import LogisticRegression
import numpy as np
from data_base_folder import data_base_logic

model = LogisticRegression()
is_trained = False

def prepare_data(history, window_size=3):
    X = []
    y = []
    for i in range(len(history) - window_size):
        X.append(history[i:i+window_size])
        y.append(history[i+window_size])
    return np.array(X), np.array(y)

def train_model(login):
    global is_trained
    history = data_base_logic.get_choices(login)
    if len(history) < 10:
        return  # мало данных — не обучаем

    X, y = prepare_data(history)
    model.fit(X, y)
    is_trained = True

def predict(history):
    if not is_trained or len(history) < 3:
        from random import randint
        return randint(1, 6)

    last_window = np.array(history[-3:]).reshape(1, -1)
    return int(model.predict(last_window)[0])
