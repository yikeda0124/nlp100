import torch
from q71 import SLPNet
from torch import nn

if __name__ == '__main__':
    model = SLPNet(300, 4)

    X_train = torch.load('/root/work/nlp100/chap8/X_train.pt')
    y_train = torch.load('/root/work/nlp100/chap8/y_train.pt')

    criterion = nn.CrossEntropyLoss()
    l_1 = criterion(model(X_train[:1]), y_train[:1]) 
    model.zero_grad()  
    l_1.backward() 
    print(f'損失: {l_1:.4f}')
    print(f'勾配:\n{model.fc.weight.grad}')

    l = criterion(model(X_train[:4]), y_train[:4])
    model.zero_grad()
    l.backward()
    print(f'損失: {l:.4f}')
    print(f'勾配:\n{model.fc.weight.grad}')