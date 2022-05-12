import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    df = pd.read_csv('newsCorpora.csv', header=None, sep='\t', names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

    df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['TITLE', 'CATEGORY']]

    train, valid_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=123, stratify=df['CATEGORY'])
    valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=123, stratify=valid_test['CATEGORY'])
    return train, valid, test    


if __name__ == '__main__':

    train, valid, test = load_data()

    train.to_csv('train.txt', sep='\t', index=False)
    valid.to_csv('valid.txt', sep='\t', index=False)
    test.to_csv('test.txt', sep='\t', index=False)

    print('train')
    print(train['CATEGORY'].value_counts())
    print('vaild')
    print(valid['CATEGORY'].value_counts())
    print('test')
    print(test['CATEGORY'].value_counts())