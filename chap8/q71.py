import torch
from torch import nn

class SLPNet(nn.Module):
  def __init__(self, input_size, output_size):
    super().__init__()
    self.fc = nn.Linear(input_size, output_size, bias=False)
    nn.init.normal_(self.fc.weight, 0.0, 1.0) 

  def forward(self, x):
    x = self.fc(x)
    return x

if __name__ == '__main__':
    model = SLPNet(300, 4)
    X_train = torch.load('/root/work/nlp100/chap8/X_train.pt')

    y_hat_1 = torch.softmax(model(X_train[:1]), dim=-1)
    print(y_hat_1)

    Y_hat = torch.softmax(model.forward(X_train[:4]), dim=-1)
    print(Y_hat)