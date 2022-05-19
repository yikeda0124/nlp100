import torch
from q71 import SLPNet
from q73 import load_file, NewsDataset
from torch import nn
from torch.utils.data import DataLoader

def calculate_accuracy(model, loader):
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model(inputs)
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels.to(device)).sum().item()

    return correct / total

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

    acc_train = calculate_accuracy(model, dataloader_train)
    acc_test = calculate_accuracy(model, dataloader_test)
    print(f'正解率（学習データ）：{acc_train:.3f}')
    print(f'正解率（評価データ）：{acc_test:.3f}')  
