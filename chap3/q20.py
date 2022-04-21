import pandas as pd

def load_json(filename):
    df = pd.read_json(filename, lines=True)
    return df[df['title']=='イギリス']['text'].values[0]

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    print(article)
