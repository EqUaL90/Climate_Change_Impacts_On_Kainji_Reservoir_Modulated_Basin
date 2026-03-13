import numpy as np

def sliding_window(series, window=12):

    X, y = [], []

    for i in range(len(series) - window):
        X.append(series[i:i+window])
        y.append(series[i+window])

    X = np.expand_dims(np.array(X), -1)
    y = np.array(y)

    return X, y