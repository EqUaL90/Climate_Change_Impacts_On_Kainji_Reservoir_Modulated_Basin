from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam

from scikeras.wrappers import KerasRegressor
from skopt import BayesSearchCV
from skopt.space import Real, Integer


def build_lstm_model(n_lstm_units=64, learning_rate=0.001, dropout_rate=0.2):

    model = Sequential([
        LSTM(n_lstm_units, activation='relu', input_shape=(12,1)),
        Dropout(dropout_rate),
        Dense(1)
    ])

    optimizer = Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss='mse'
    )

    return model


def optimize_lstm(X_train, y_train):

    model_wrapper = KerasRegressor(
        model=build_lstm_model,
        epochs=20,
        verbose=0
    )

    search_space = {

        "model__n_lstm_units": Integer(32,128),
        "model__learning_rate": Real(1e-5,1e-2,prior='log-uniform'),
        "model__dropout_rate": Real(0.1,0.5),
        "batch_size": Integer(16,64)

    }

    opt = BayesSearchCV(
        estimator=model_wrapper,
        search_spaces=search_space,
        n_iter=15,
        cv=3,
        random_state=42
    )

    opt.fit(X_train,y_train)

    return opt