import torch
from q71 import SLPNet
from torch import nn
from torch.utils.data import Dataset, DataLoader

def load_file(dir):
    X_train = torch.load(dir + 'X_train.pt')
    X_valid = torch.load(dir + 'X_valid.pt')
    X_test = torch.load(dir + 'X_test.pt')
    y_train = torch.load(dir + 'y_train.pt')
    y_valid = torch.load(dir + 'y_valid.pt')
    y_test = torch.load(dir + 'y_test.pt')

    return X_train, X_valid, X_test, y_train, y_valid, y_test


class NewsDataset(Dataset):
  def __init__(self, X, y): 
    self.X = X
    self.y = y

  def __len__(self): 
    return len(self.y)

  def __getitem__(self, idx):
    return [self.X[idx], self.y[idx]]


if __name__ == '__main__':
    X_train, X_valid, X_test, y_train, y_valid, y_test = load_file('/root/work/nlp100/chap8/')

    dataset_train = NewsDataset(X_train, y_train)
    dataset_valid = NewsDataset(X_valid, y_valid)
    dataset_test = NewsDataset(X_test, y_test)

    dataloader_train = DataLoader(dataset_train, batch_size=1, shuffle=True)
    dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
    dataloader_test = DataLoader(dataset_test, batch_size=len(dataset_test), shuffle=False)

    model = SLPNet(300, 4)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)

    num_epochs = 10
    for epoch in range(num_epochs):
        model.train()
        loss_train = 0.0
        for i, (inputs, labels) in enumerate(dataloader_train):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            loss_train += loss.item()

        loss_train = loss_train / i

        model.eval() 
        with torch.no_grad():
            inputs, labels = next(iter(dataloader_valid))
            outputs = model(inputs)
            loss_valid = criterion(outputs, labels)

        print(f'epoch: {epoch + 1}, loss_train: {loss_train:.4f}, loss_valid: {loss_valid:.4f}')  
