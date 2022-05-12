import numpy as np
import pandas as pd
from q52 import train

if __name__ == '__main__':
    lg = train()
    X_train = pd.read_csv('train.feature.txt', sep='\t')
    features = X_train.columns.values
    index = [i for i in range(1, 11)]
    for c, coef in zip(lg.classes_, lg.coef_):
        print(f'【カテゴリ】{c}')
        best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['重要度上位'], index=index).T
        worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['重要度下位'], index=index).T
        print(pd.concat([best10, worst10], axis=0))
        print('\n')