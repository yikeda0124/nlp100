from tqdm import tqdm
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from q50 import load_data
from q53 import score_lg
import matplotlib.pyplot as plt

if __name__ == '__main__':
    train, valid, test = load_data()
    X_train = pd.read_csv('train.feature.txt', sep='\t')
    X_valid = pd.read_csv('valid.feature.txt', sep='\t')
    X_test = pd.read_csv('test.feature.txt', sep='\t')
    result = []
    for C in tqdm(np.logspace(-5, 4, 10, base=10)):
        # モデルの学習
        lg = LogisticRegression(random_state=123, max_iter=10000, C=C)
        lg.fit(X_train, train['CATEGORY'])

        # 予測値の取得
        train_pred = score_lg(lg, X_train)
        valid_pred = score_lg(lg, X_valid)
        test_pred = score_lg(lg, X_test)

        # 正解率の算出
        train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
        valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])
        test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])

        # 結果の格納
        result.append([C, train_accuracy, valid_accuracy, test_accuracy])
    
    result = np.array(result).T
    plt.plot(result[0], result[1], label='train')
    plt.plot(result[0], result[2], label='valid')
    plt.plot(result[0], result[3], label='test')
    plt.ylim(0, 1.1)
    plt.ylabel('Accuracy')
    plt.xscale ('log')
    plt.xlabel('C')
    plt.legend()
    plt.show()