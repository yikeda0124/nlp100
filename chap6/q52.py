from sklearn.linear_model import LogisticRegression
import pandas as pd
from q50 import load_data

def train():
    train, valid, test = load_data()
    X_train = pd.read_csv('train.feature.txt', sep='\t')
    # モデルの学習
    print('start training')
    lg = LogisticRegression(random_state=123, max_iter=10000)
    lg.fit(X_train, train['CATEGORY'])
    print('done training')
    return lg

if __name__ == '__main__':
    train()