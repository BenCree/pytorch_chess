import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch import optim

class ChessDataset(Dataset):
    def __init__(self, dat):
        dat = np.load(dat)
        print(dat.keys())
        self.X = torch.tensor(dat['arr_0'], dtype=torch.float32)
        self.Y = torch.tensor(dat['arr_1'], dtype=torch.float32)
        print(self.Y)
        print('dataset: ', self.X.shape, self.Y.shape)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]

    def __len__(self):
        return self.X.shape[0]

class ChessNet(nn.Module):
    def __init__(self):
        super(ChessNet, self).__init__()
        self.fc1 = nn.Linear(69, 128)
        self.conv1 = nn.Conv2d(69, 69, kernel_size=3)# First layer
        self.fc2 = nn.Linear(128, 64)
        self.conv2 = nn.Conv2d(69, 69, kernel_size=3)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = ChessNet()

criterion = loss = torch.nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.0001, momentum=0.9)

dat = ChessDataset('1000_training_data.npz')

testloader = DataLoader(dat, num_workers=8)

for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(testloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')