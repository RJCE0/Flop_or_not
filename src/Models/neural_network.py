import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
from ...Database.PreProcessing.data_loading import X, y, unseparated_data, FBRefDataset, seperate_labels_and_inputs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# set up the GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyperparameters
dimensions = [28, 1570, 970, 810, 510, 13]
num_epochs = 750
batch_size = 32
learning_rate = 0.0005
# adam hyperparameters
betas = (0.9, 0.999)
eps = 2e-8
weight_decay = 0.0005
amsgrad = False

# get the data
dataset = FBRefDataset()

# do a train test split
train_data, test_data = train_test_split(dataset, test_size=0.25, random_state=42)

# fit into a dataloader objects
trainloader = data.DataLoader(
    train_data, 
    batch_size=batch_size, 
    shuffle=True, 
    pin_memory=True)

testloader = data.DataLoader(
    test_data, 
    batch_size=batch_size, 
    shuffle=True, 
    pin_memory=True)

# Define your neural network model
class NeuralNetwork(nn.Module):
    def __init__(self, dimensions):
        super(NeuralNetwork, self).__init__()

        self.fc1 = nn.Linear(dimensions[0], dimensions[1])
        self.fc2 = nn.Linear(dimensions[1], dimensions[2])
        self.fc3 = nn.Linear(dimensions[2], dimensions[3])
        self.fc4 = nn.Linear(dimensions[3], dimensions[-1])
        self.tanh = nn.Tanh()
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.tanh(out)
        out = self.fc2(out)
        out = self.tanh(out)
        out = self.fc3(out)
        out = self.tanh(out)
        out = self.fc4(out)
        return out

# Training 
def train(model, num_epochs, loss_func, optimisation_func, train_loader):
    loss_list = []
    total_step = len(train_loader)

    for epoch in range(num_epochs):
        running_loss = 0
        
        for i, (inputs, labels) in enumerate(train_loader):
            inputs = inputs.to(device)
            labels = labels.to(device)
            
            # Forward pass
            outputs = model(inputs)
            loss = loss_func(labels, outputs)
            running_loss += loss.item()

            # Backward and optimize
            optimisation_func.zero_grad()
            loss.backward()
            optimisation_func.step()

        loss_list.append(np.mean(running_loss))
        if (epoch+1) % 1_00 == 0:
            print(f'Epoch [Prev > {epoch+1}], Loss: {np.mean(running_loss)}')
            # add the last n epochs to a list

        # TODO implement early stopping criterion
        # if : then ...
        
    plt.title("Loss against epochs")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.plot(loss_list)
    plt.show()



neural_newtork = NeuralNetwork(dimensions)
neural_newtork = neural_newtork.to(device)

# Optimisation and Loss function setup
loss_function = nn.MSELoss()
optimisation_function = optim.Adam(
    neural_newtork.parameters(),
    lr=learning_rate,
    betas=betas,
    eps=eps,
    weight_decay=weight_decay,
    amsgrad=amsgrad
)

train(
    model=neural_newtork,
    num_epochs=num_epochs,
    loss_func=loss_function,
    optimisation_func=optimisation_function,
    train_loader=trainloader
    )

# Fixed number ----------------------------------------------------------------
tolerence = 2
valid = 0
total = 0
# Test the model 3
predictions = []
actual = []
neural_newtork.eval()
for batch_data, batch_labels in testloader:
    
    batch_data, batch_labels = batch_data.to(device), batch_labels.to(device)
    neural_newtork.eval()
    
    with torch.no_grad():
        i = 0

        # print the predicted outputs
        outputs = neural_newtork(batch_data)
        outputs = outputs.to(device)
        
        # Algo----------------
        # get a batch 
        # loop through it
        # for every prediction in the batch, compare to the corresponding label
        # if its within a certain threshold, iterate a "valid" variable
        # once you get to the end, divide the valid variable by the total to get accuracy

        # all labels
        for i in range(len(batch_labels)):

            all_labels = batch_labels[i]
            single_prediction = outputs[i]
            

            pred = max(0, single_prediction[5].to(device).item())
            label = all_labels[5].to(device).item()
            
            print(f"Acc: {all_labels[5]} Pred: {pred:.2f}")
            
            predictions.append(pred)
            actual.append(label)

            if all_labels[5] - tolerence < pred < all_labels[5] + tolerence:
                valid += 1 
            
            total += 1            



print(valid)
print(total)
print(valid/total)
print(f"The accuracy of the model with {num_epochs} epochs and target range of {tolerence} goal is: {valid/total}")
rmse = np.sqrt(mean_squared_error(predictions, actual))
print(f"Teh RMSE is {rmse}")
# print(predictions)
# print(actual)
