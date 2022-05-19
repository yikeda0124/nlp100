from chap6.q50 import load_data
import gdown
from gensim.models import KeyedVectors
import string
import torch

def transform_w2v(model, text):
  table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
  words = text.translate(table).split()
  vec = [model[word] for word in words if word in model]

  return torch.tensor(sum(vec) / len(vec))



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

    url = "https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM"
    output = 'GoogleNews-vectors-negative300.bin.gz'
    gdown.download(url, output, quiet=True)

    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

    X_train = torch.stack([transform_w2v(model, text) for text in train['TITLE']])
    X_valid = torch.stack([transform_w2v(model, text) for text in valid['TITLE']])
    X_test = torch.stack([transform_w2v(model, text) for text in test['TITLE']])

    print(X_train.size())
    print(X_train)

    category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
    y_train = torch.tensor(train['CATEGORY'].map(lambda x: category_dict[x]).values)
    y_valid = torch.tensor(valid['CATEGORY'].map(lambda x: category_dict[x]).values)
    y_test = torch.tensor(test['CATEGORY'].map(lambda x: category_dict[x]).values)

    print(y_train.size())
    print(y_train)

    torch.save(X_train, '/root/work/nlp100/chap8/X_train.pt')
    torch.save(X_valid, '/root/work/nlp100/chap8/X_valid.pt')
    torch.save(X_test, '/root/work/nlp100/chap8/X_test.pt')
    torch.save(y_train, '/root/work/nlp100/chap8/y_train.pt')
    torch.save(y_valid, '/root/work/nlp100/chap8/y_valid.pt')
    torch.save(y_test, '/root/work/nlp100/chap8/y_test.pt')