import numpy as np
import pandas as pd
from q50 import load_data
from q52 import train

def score_lg(lg, X):
    return [np.max(lg.predict_proba(X), axis=1), lg.predict(X)]

if __name__ == '__main__':
    lg = train()
    train, valid, test = load_data()
    X_train = pd.read_csv('train.feature.txt', sep='\t')
    X_test = pd.read_csv('test.feature.txt', sep='\t')

    train_pred = score_lg(lg, X_train)

    print(train_pred)