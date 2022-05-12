import optuna
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from q50 import load_data
from q53 import score_lg
import pandas as pd

train, valid, test = load_data()
X_train = pd.read_csv('train.feature.txt', sep='\t')
X_valid = pd.read_csv('valid.feature.txt', sep='\t')
X_test = pd.read_csv('test.feature.txt', sep='\t')

def objective_lg(trial):
    # チューニング対象パラメータのセット
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
    C = trial.suggest_loguniform('C', 1e-4, 1e4)

    # モデルの学習
    lg = LogisticRegression(random_state=123, 
                            max_iter=10000, 
                            penalty='elasticnet', 
                            solver='saga', 
                            l1_ratio=l1_ratio, 
                            C=C)
    lg.fit(X_train, train['CATEGORY'])

    # 予測値の取得
    valid_pred = score_lg(lg, X_valid)

    # 正解率の算出
    valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])    

    return valid_accuracy 

if __name__ == '__main__':
    
    study = optuna.create_study(direction='maximize')
    study.optimize(objective_lg, timeout=100)

    # 結果の表示
    print('Best trial:')
    trial = study.best_trial
    print('  Value: {:.3f}'.format(trial.value))
    print('  Params: ')
    for key, value in trial.params.items():
        print('    {}: {}'.format(key, value))

    # パラメータの設定
    l1_ratio = trial.params['l1_ratio']
    C = trial.params['C']

    # モデルの学習
    lg = LogisticRegression(random_state=123, 
                            max_iter=10000, 
                            penalty='elasticnet', 
                            solver='saga', 
                            l1_ratio=l1_ratio, 
                            C=C)
    lg.fit(X_train, train['CATEGORY'])

    # 予測値の取得
    train_pred = score_lg(lg, X_train)
    valid_pred = score_lg(lg, X_valid)
    test_pred = score_lg(lg, X_test)

    # 正解率の算出
    train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1]) 
    valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1]) 
    test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1]) 

    print(f'正解率（学習データ）：{train_accuracy:.3f}')
    print(f'正解率（検証データ）：{valid_accuracy:.3f}')
    print(f'正解率（評価データ）：{test_accuracy:.3f}')