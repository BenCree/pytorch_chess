import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch import optim

class ChessDataset(Dataset):
    def __init__(self):
        dat = np.load('dataset.npz')
        self.X = dat[0]
        self.Y = dat[1]
        print('dataset: ', self.X.shape, self.Y.shape)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]

    def __len__(self):
        return self.X.shape[0]

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #things

    def forward(self, x):
        #things
        return x