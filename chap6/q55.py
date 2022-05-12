from sklearn.metrics import confusion_matrix
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
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

    train_cm = confusion_matrix(train['CATEGORY'], train_pred[1])
    print(train_cm)
    sns.heatmap(train_cm, annot=True, cmap='Blues')
    plt.show()

    test_cm = confusion_matrix(test['CATEGORY'], test_pred[1])
    print(test_cm)
    sns.heatmap(test_cm, annot=True, cmap='Blues')
    plt.show()