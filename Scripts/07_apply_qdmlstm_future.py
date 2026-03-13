def apply_qdmlstm(qdm_series, lstm_model, window=12):

    corrected = []

    for i in range(len(qdm_series) - window):

        X = qdm_series[i:i+window]
        X = X.reshape(1, window, 1)

        residual = lstm_model.predict(X)[0]

        corrected.append(qdm_series[i+window] + residual)

    return corrected