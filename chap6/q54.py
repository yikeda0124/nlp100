from sklearn.metrics import accuracy_score
import pandas as pd
from q50 import load_data
from q52 import train
from q53 import score_lg

if __name__ == '__main__':
    lg = train()
    train, valid, test = load_data()
    X_train = pd.read_csv('train.feature.txt', sep='\t')
    X_test = pd.read_csv('test.feature.txt', sep='\t')

    train_pred = score_lg(lg, X_train)
    test_pred = score_lg(lg, X_test)

    train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
    test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])
    print(f'正解率（学習データ）：{train_accuracy:.3f}')
    print(f'正解率（評価データ）：{test_accuracy:.3f}')