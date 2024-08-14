import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

torch.manual_seed(0)
X = np.random.rand(200, 2)*10
y = (X[:, 0] + X[:, 1] > 10).astype(int)

X_tensor = torch.tensor(X).float()
y_tensor = torch.tensor(y).float().unsqueeze(1)
X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.20, random_state=0)


class NN(nn.Module):
    def __init__(self):
        super(NN, self).__init__()

        self.input_layer = nn.Linear(2, 32)
        self.hidden_layer = nn.Linear(32, 32)
        self.output_layer = nn.Linear(32, 1)
    
    def forward(self, x):
        x = torch.relu(self.input_layer(x))
        x = torch.relu(self.hidden_layer(x))
        x = torch.sigmoid(self.output_layer(x))
        return x

model = NN()
loss_func = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
losses = []

for epoch in range(8000):
    optimizer.zero_grad()

    y_pred = model(X_train)
    loss = loss_func(y_pred, y_train)
    
    loss.backward()
    optimizer.step()

    print("Loss: ", loss)
    losses.append(loss.item())

def get_acc(y_test_pred, test_y):
    total = 0
    for i in range(len(y_test_pred)):
        if y_test_pred[i] == test_y[i]:
            total+=1
    return total/len(y_test_pred)


y_test_pred = model(X_test)
acc = get_acc(y_test_pred, y_test)
print(f"Accuracy: {acc*100}%")

plt.plot(losses)
plt.show()